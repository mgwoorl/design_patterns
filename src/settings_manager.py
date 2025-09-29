"""
Менеджер настроек приложения
"""

import os
import json
from src.models.settings import Settings
from src.models.company_model import company_model
from src.core.validator import operation_exception

class SettingsManager:
    __file_name: str = ""
    __settings: Settings = None
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SettingsManager, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.__settings = Settings()
            self._initialized = True

    """ Текущие настройки """
    @property
    def settings(self) -> Settings:
        return self.__settings

    """ Открывает файл настроек """
    def open(self, file_path: str) -> bool:
        return self.load(file_path)

    """ Загружает настройки из файла """
    def load(self, file_path: str = None) -> bool:
        if file_path:
            self.__file_name = file_path

        if not self.__file_name:
            raise operation_exception("Файл не указан")

        try:
            with open(self.__file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.convert(data)
            return True
        except Exception as error:
            print(f"Ошибка загрузки: {error}")
            return False

    """ Конвертирует данные JSON в модель настроек """
    def convert(self, data: dict):
        company = company_model()
        company_data = data.get("company", {})

        company.name = company_data.get("name", "")
        company.inn = company_data.get("inn", "")
        company.bik = company_data.get("bik", "")
        company.account = company_data.get("account", "")
        company.correspondent_account = company_data.get("correspondent_account", "")
        company.ownership = company_data.get("ownership", "")

        self.__settings.company = company
