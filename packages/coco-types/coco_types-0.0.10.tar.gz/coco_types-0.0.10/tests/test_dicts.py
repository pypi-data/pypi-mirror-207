import json
from pathlib import Path

import coco_types


def test_parse_object_detection() -> None:
    with Path("data_samples/coco_25k_object_detection/annotations.json").open(encoding="utf-8") as data_file:
        dataset: coco_types.dicts.Dataset = json.load(data_file)

    assert dataset["images"][0]["file_name"] == "000000174482.jpg"
    assert dataset["annotations"][0]["bbox"] == [187.74, 5.84, 310.4, 380.49]
    assert dataset["categories"][0]["name"] == "person"


def test_parse_keypoints() -> None:
    with Path("data_samples/val2017_keypoints_samples/annotations.json").open(encoding="utf-8") as data_file:
        dataset: coco_types.dicts.DatasetKP = json.load(data_file)

    assert dataset["images"][0]["file_name"] == "000000000785.jpg"
    assert dataset["annotations"][0]["bbox"] == [280.79, 44.73, 218.7, 346.68]
    assert dataset["categories"][0]["name"] == "person"


def test_instantiate_image() -> None:
    img_entry = coco_types.dicts.Image(id=1, width=320, height=320, file_name="test.png")
    assert img_entry["id"] == 1
