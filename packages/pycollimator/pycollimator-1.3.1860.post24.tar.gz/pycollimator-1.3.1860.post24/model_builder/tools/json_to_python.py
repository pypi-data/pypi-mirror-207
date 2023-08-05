import argparse
import json

from pycollimator.model_builder import from_json
from pycollimator.model_builder.to_python import to_python_str


if __name__ == "__main__":
    """
    Usage:
        bazel run //src/lib/pycollimator/model_builder/tools:json_to_python -- models/double_bouncing_ball.json
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", type=str, help="path to JSON file")
    args = parser.parse_args()

    with open(args.filepath) as f:
        in_json_data = json.load(f)

        model_builder, uuids, uiprops = from_json.parse_json(in_json_data)
        print(to_python_str(model_builder))
