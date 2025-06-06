import json
from pathlib import Path
from typing import Dict, Any, OrderedDict

def load_json_file(path:str) -> Dict[str, Any]:
    file_path = Path(path)
    if not file_path.is_file():
        raise FileNotFoundError(f"No such file: {file_path}")
    
    with file_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Expected top-level object to be a dict, got {type(data)}")
    return data

def sort_dict_by_value(
        data:Dict[str, Any],
        reverse:bool=False
):
    sorted_items = sorted(data.items(), key=lambda kv:kv[1], reverse=reverse)
    from collections import OrderedDict
    return OrderedDict(sorted_items)

def rewrite_to_json_file(data:Dict[str, Any], indent:int=4):
    return json.dumps(data, indent=indent, ensure_ascii=False)