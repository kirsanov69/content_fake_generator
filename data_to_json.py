
"""
Принимаем структуру из data_to_json.py и преобразуем ее в JSON-ответ для фронта.
компоненты:

text_block - для title, text, quote

action_button - для button

Компоненты объединяются по parent_block_id - общий id блока, к которому они принадлежат.("block-0-0")

title - заголовок или надпись
data - основной текст
status - 'nice' для текста, 'normal' для кнопки
severity — та же важность, что была в исходных данных
список списков, где каждый список — это блок с элементами, которые имеют общий parent_block_id.
"""


from collections import defaultdict
import json
from typing import List, Dict, Any

def convert_to_json(response: List[Dict[str, Any]], component_block: str = "block-0-0") -> str:
    
    item_type_to_component: Dict[str, str] = {
        "title": "text_block",
        "text": "text_block",
        "quote": "text_block",
        "image": "picture_block",
        "img": "picture_block",
        "button": "action_button",
    }

    
    component_status: Dict[str, str] = {
        "text_block": "nice",
        "action_button": "normal",
        "picture_block": "normal"
    }

    # Группируем по parent_block_id и component_name
    grouped_blocks = defaultdict(lambda: defaultdict(list))

    for item in response[0]:
        block_id = item.get("parent_block_id", component_block)
        item_type = item.get("item_type", "")
        component_name = item_type_to_component.get(item_type)

        if not component_name:
            continue

        items = item.get("items", [item])

        for sub_item in items:
            item_dict = {
                "title": sub_item.get("item_title", sub_item.get("item_data", "")),
                "data": sub_item.get("item_data", ""),
                "severity": sub_item.get("item_severity", 2),
            }

            if component_name != "picture_block":
                item_dict["status"] = component_status[component_name]
            else:
                item_dict["src"] = sub_item.get("item_data", ""),
                item_dict["alt"] = "Не удалось загрузить изображение"

            grouped_blocks[block_id][component_name].append(item_dict)

    
    result = []
    for block_id, components in grouped_blocks.items():
        for component_name, items in components.items():
            result.append({
                "component_name": component_name,
                "parent_block_id": block_id,
                "items": items
            })

    return json.dumps(result, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from generate_response import generate_response
    response = generate_response()
    print("Response generated successfully.", response)
    json_output = convert_to_json(response, "block-0-1")
    print(json_output)