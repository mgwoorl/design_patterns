from src.core.abstract_response import abstract_response
from src.logics.response_csv import response_csv
from src.logics.response_markdown import response_markdown
from src.logics.response_json import response_json
from src.logics.response_xml import response_xml
from src.core.validator import operation_exception
from src.models.settings_model import settings_model, ResponseFormat

class factory_entities:
    __match = {
        "csv": response_csv,
        "markdown": response_markdown,
        "json": response_json,
        "xml": response_xml
    }
    
    __settings: settings_model

    def __init__(self, settings: settings_model):
        self.__settings = settings

    # Получить нужный тип по формату
    def create(self, format: str) -> abstract_response:
        if format not in self.__match.keys():
            raise operation_exception("Формат не верный")
        
        return self.__match[format]()

    # Создать ответ по настройкам
    def create_default(self, data: list) -> abstract_response:
        format_type = self.__settings.response_format.value
        return self.create(format_type)
