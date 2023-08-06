import json
from dataclasses import asdict, is_dataclass
from datetime import date, datetime


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)


def try_str_to_float(text: str) -> any:
    try:
        return float(text)
    except ValueError:
        return text


def function_exists(cls, name: str) -> bool:
    try:
        return callable(getattr(cls, name))
    except:
        return False
