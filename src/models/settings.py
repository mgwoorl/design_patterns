from src.models.company_model import company_model

class settings:
    __company: company_model = None

    def __init__(self):
        self.__company = company_model()

    @property
    def company(self) -> company_model:
        return self.__company
