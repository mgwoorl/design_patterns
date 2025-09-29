from src.models.company_model import company_model
from src.core.validator import validator

class Settings:
    __company: company_model = None

    def __init__(self):
        self.__company = company_model()

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value: company_model):
        validator.validate(value, company_model)
        self.__company = value
