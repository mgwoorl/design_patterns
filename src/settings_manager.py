import os
import json
from src.models.settings import Settings
from src.models.company_model import CompanyModel

class SettingsManager:
    __file_name: str = ""
    __settings: Settings = None

    def __new__(cls, file_name: str = ""):
        if not hasattr(cls, "instance"):
            cls.instance = super(SettingsManager, cls).__new__(cls)
        return cls.instance

    def __init__(self, file_name: str = ""):
        self.__settings = Settings()
        self.set_default()
        if file_name:
            self.file_name = file_name

    @property
    def settings(self) -> Settings:
        return self.__settings

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, value: str):
        if not value.strip():
            return

        if os.path.exists(value):
            self.__file_name = os.path.abspath(value)
            return

        src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), value))
        if os.path.exists(src_path):
            self.__file_name = src_path
            return

        project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", value))
        if os.path.exists(project_root_path):
            self.__file_name = project_root_path
            return

        raise FileNotFoundError(f"Файл с настройками не найден: {value}")

    def load(self, file_path: str = None) -> bool:
        if file_path:
            self.file_name = file_path

        if not self.__file_name.strip():
            raise FileNotFoundError("Файл с настройками не указан!")

        try:
            with open(self.__file_name, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.convert(data)
            return True
        except Exception as error:
            print(f"Ошибка загрузки настроек: {error}")
            return False

    def convert(self, data: dict):
        company = CompanyModel()
        company_data = data.get("company", {})

        company.name = company_data.get("name", "")
        company.inn = company_data.get("inn", "")
        company.account = company_data.get("account", "")
        company.correspondent_account = company_data.get("correspondent_account", "")
        company.bik = company_data.get("bik", "")
        company.ownership = company_data.get("ownership", "")

        self.__settings._Settings__company = company

    def set_default(self):
        self.__settings = Settings()
        self.__settings.company.name = "Default"
        self.__settings.company.inn = "000000000000" 
        self.__settings.company.account = "00000000000"  
        self.__settings.company.correspondent_account = "00000000000"  
        self.__settings.company.bik = "000000000" 
        self.__settings.company.ownership = "OOO"
