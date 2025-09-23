import os
import json
from src.models.company_model import company_model
from src.models.settings import settings

class settings_manager:
    __file_name: str = ""
    __settings: settings = None

    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.set_default()

    @property
    def settings(self) -> settings:
        return self.__settings

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, value: str):
        if not value.strip():
            return
        abs_path = os.path.abspath(value.strip())
        if os.path.exists(abs_path):
            self.__file_name = abs_path
        else:
            raise FileNotFoundError("Файл с настройками не найден!")

    def load(self) -> bool:
        if not self.__file_name.strip():
            raise FileNotFoundError("Файл с настройками не указан!")

        try:
            with open(self.__file_name, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.convert(data)
            return True

        except Exception as ex:
            print(f"Ошибка загрузки настроек для компании: {ex}")
            return False

    def convert(self, data: dict):
        self.__settings = settings()
        company = company_model()

        company_data = data.get("company", {})

        company.name = company_data.get("name", "")
        company.inn = company_data.get("inn", "")
        company.account = company_data.get("account", "")
        company.correspondent_account = company_data.get("correspondent_account", "")
        company.bik = company_data.get("bik", "")
        company.ownership = company_data.get("ownership", "")

        self.__settings._settings__company = company

    def set_default(self):
        self.__settings = settings()
        self.__settings.company.name = "Default"
