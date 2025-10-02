"""
Модель настроек приложения
"""

from src.models.company_model import company_model
from src.core.validator import validator

class Settings:
    __company: company_model = None

    def __init__(self):
        self.__company = company_model()

    """ Текущая организация """
    @property
    def company(self) -> company_model:
        return self.__company
    
    """ Устанавливает текущую организацию """
    @company.setter
    def company(self, value: company_model):
        validator.validate(value, company_model)
        self.__company = value
