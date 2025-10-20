from src.core.abstract_response import abstract_response
from src.core.common import common
from src.core.validator import validator, operation_exception

class response_markdown(abstract_response):
    def build(self, data: list) -> str:
        super().build(data)
        
        if len(data) == 0:
            return ""
            
        text = ""
        # Шапка таблицы
        item = data[0]
        fields = common.get_fields(item)
        text += "| " + " | ".join(fields) + " |\n"
        text += "|" + "|".join(["---"] * len(fields)) + "|\n"
        
        # Данные
        for item in data:
            row = []
            for field in fields:
                value = getattr(item, field, "")
                row.append(str(value))
            text += "| " + " | ".join(row) + " |\n"
            
        return text
