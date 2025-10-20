from src.core.abstract_response import abstract_response
from src.core.common import common
from src.core.validator import validator, operation_exception
import json

class response_json(abstract_response):
    def build(self, data: list) -> str:
        super().build(data)
        
        result = []
        for item in data:
            item_dict = {}
            fields = common.get_fields(item)
            for field in fields:
                item_dict[field] = getattr(item, field, None)
            result.append(item_dict)
            
        return json.dumps(result, ensure_ascii=False, indent=2)
