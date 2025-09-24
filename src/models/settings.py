from src.models.company_model import CompanyModel

class Settings:
    __company: CompanyModel = None

    def __init__(self):
        self.__company = CompanyModel()

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value: CompanyModel):
        if not isinstance(value, CompanyModel):
            raise TypeError("Ожидается объект CompanyModel")
        self.__company = value
