from src.models.company_model import company_model
import os
import json

class settings_manager:
    __file_name:str = ""
    __company:company_model = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(settings_manager, cls).__new__(cls)
        return cls.instance 
    
    def __init__(self):
        self.set_default()

    @property
    def company(self) -> company_model:
        return self.__company

    @property
    def file_name(self) -> str:
        return self.__file_name

    @file_name.setter
    def file_name(self, value:str):
        if value.strip() == "":
            return
        
        if os.path.exists(value):
            self.__file_name = value.strip()
        else:
            raise Exception("Не найден файл настроек!")

    def load(self) -> bool:
        if self.__file_name.strip() == "":
            raise Exception("Не найден файл настроек!")

        try:
            with open( self.__file_name.strip(), 'r') as file_instance:
                data = json.load(file_instance)

                if "company" in data.keys():
                    item = data["company"]
                
                    self.__company.name = item["name"]
                    return True

            return False
        except:
            return False

    #по умолчанию
    def set_default(self):
        self.__company = company_model()
        self.__company.name = "Ирис"