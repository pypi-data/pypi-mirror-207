# Copyright 2022 The Kubeflow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Component for converting classification text dataset for batch prediction."""
from typing import List, NamedTuple
from kfp import dsl


@dsl.component(
    base_image="us-docker.pkg.dev/vertex-ai/training/tf-cpu.2-8:latest"
)
def convert_dataset_export_for_batch_predict(
    file_paths: List[str],
    classification_type: str,
    output_dir: dsl.OutputPath(list),
) -> NamedTuple("Outputs", [("output_files", list)]):
  """Converts classification dataset export for batch prediction input.

  For each processed data item, there will be a JSON object with two fields: a
  text field containing the raw text (either passed in directly or read from
  GCS), and either a single string label or list of string labels, depending on
  the classification type.

  Args:
    file_paths: List of URIs of the files storing the batch prediction input.
    classification_type: String representing the problem type: either
      "multiclass" (single-label) or "multilabel".
    output_dir: GCS directory where the output files will be stored. Should be
      generated by the pipeline.

  Returns:
    Namedtuple of one list under "output_files" key, containing the URIs of the
    JSONL files ready to be consumed by Vertex batch prediction.
  """
  # pylint: disable=g-import-not-at-top
  import collections
  import json
  import os
  import tensorflow as tf
  # pylint: enable=g-import-not-at-top

  # pylint: disable=invalid-name
  MULTILABEL_TYPE = "multilabel"
  TEXT_KEY = "text"
  LABELS_KEY = "labels"
  CLASSIFICATION_ANNOTATION_KEY = "classificationAnnotation"
  CLASSIFICATION_ANNOTATIONS_KEY = "classificationAnnotations"
  DISPLAY_NAME_KEY = "displayName"
  CONTENT_KEY = "textContent"
  GCS_URI_KEY = "textGcsUri"
  # pylint: enable=invalid-name

  output_file_paths = []
  for file_path in file_paths:
    with tf.io.gfile.GFile(file_path) as json_file:
      # Ensure all dirs are present.
      output_file_path = os.path.join(output_dir, os.path.basename(file_path))
      os.makedirs(output_dir, exist_ok=True)

      with tf.io.gfile.GFile(output_file_path, "w") as results_file:
        for dataset_line in json_file:
          json_obj = json.loads(dataset_line)
          result_list = []
          if json_obj.get(CONTENT_KEY):
            result_list.append(json_obj.get(CONTENT_KEY))
          elif json_obj.get(GCS_URI_KEY):
            with tf.io.gfile.GFile(json_obj.get(GCS_URI_KEY), "r") as gcs_file:
              result_list.append(gcs_file.read())
          else:
            raise ValueError("Text content or GCS URI must be specified.")
          result_obj = {TEXT_KEY: result_list}

          if classification_type == MULTILABEL_TYPE:
            result_obj[LABELS_KEY] = [
                annotation[DISPLAY_NAME_KEY]
                for annotation in json_obj[CLASSIFICATION_ANNOTATIONS_KEY]
            ]
          else:
            result_obj[LABELS_KEY] = json_obj[CLASSIFICATION_ANNOTATION_KEY][
                DISPLAY_NAME_KEY
            ]
          results_file.write(json.dumps(result_obj) + "\n")
      # Subsequent components will not understand "/gcs/" prefix. Convert to use
      # "gs://" prefix for compatibility.
      if output_file_path.startswith("/gcs/"):
        output_file_path = "gs://" + output_file_path[5:]
      output_file_paths.append(output_file_path)
  output_tuple = collections.namedtuple("Outputs", ["output_files"])
  return output_tuple(output_file_paths)
