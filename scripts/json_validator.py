import json
from jsonschema import validate, ValidationError

class JsonValidator():
    def __init__(self):
        self.schema = {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "phases": {
                        "type": "array",
                        "items": {"type": "string"},
                        "minItems": 1
                    },
                    "note": {"type": "string"}
                },
                "required": ["phases", "note"],
                "additionalProperties": False
            }
        }

    def validate_json(self, json_file) -> bool:
        try:
            with open(json_file, "r", encoding="utf-8") as file:
                data = json.load(file)
            validate(instance=data, schema=schema)
            return True
        except ValidationError as e:
            return False
        except json.JSONDecodeError:
            return False
