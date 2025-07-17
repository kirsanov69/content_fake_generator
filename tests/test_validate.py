import pytest
import json
from typing import Any
from content_fake_generator.data_to_json import convert_to_json 

@pytest.fixture
def sample_response() -> list[list[dict[str, Any]]]:
    return [[
        {
            "item_type": "title",
            "item_data": "Тестовый заголовок",
            "item_severity": 1,
            "parent_block_id": "block-0-0"
        },
        {
            "item_type": "button",
            "items": [
                {"item_title": "Ответ 1", "item_severity": 2}
            ],
            "parent_block_id": "block-0-0"
        },
        {
            "item_type": "img",
            "item_data": {
                "src": "https://example.com/image.jpg",
                "alt": "Some image"
            },
            "item_title": "Картинка",
            "item_severity": 2,
            "parent_block_id": "block-0-2"
        }
    ]]

def test_output_is_json_string(sample_response) -> None:
    result = convert_to_json(sample_response)
    assert isinstance(result, str)
    parsed = json.loads(result)
    assert isinstance(parsed, list)

def test_top_level_keys(sample_response) -> None:
    result = json.loads(convert_to_json(sample_response))
    for block in result:
        assert set(block.keys()) <= {"component_name", "parent_block_id", "items"}

def test_component_name_values(sample_response) -> None:
    result = json.loads(convert_to_json(sample_response))
    allowed = {"text_block", "action_button", "picture_block"}
    for block in result:
        assert block["component_name"] in allowed

def test_picture_block_structure(sample_response) -> None:
    result = json.loads(convert_to_json(sample_response))
    for block in result:
        if block["component_name"] == "picture_block":
            for item in block["items"]:
                assert "status" not in item
                assert isinstance(item["data"], dict)
                assert "src" in item["data"]
                assert "alt" in item["data"]

def test_text_block_and_buttons_have_status(sample_response) -> None:
    result = json.loads(convert_to_json(sample_response))
    for block in result:
        if block["component_name"] in {"text_block", "action_button"}:
            for item in block["items"]:
                assert "status" in item
