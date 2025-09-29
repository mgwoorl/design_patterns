from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception
from src.models.settings import Settings

class company_model(abstract_reference):
    __inn: str = ""
    __bik: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __ownership: str = ""

    def __init__(self, name: str = "", settings: Settings = None):
        super().__init__(name)
        if settings and settings.company:
            self._copy_from_settings(settings.company)

    def _copy_from_settings(self, company_data):
        try:
            self.name = getattr(company_data, 'name', '')
            self.inn = getattr(company_data, 'inn', '')
            self.bik = getattr(company_data, 'bik', '')
            self.account = getattr(company_data, 'account', '')
            self.correspondent_account = getattr(company_data, 'correspondent_account', '')
            self.ownership = getattr(company_data, 'ownership', '')
        except Exception as e:
            raise argument_exception(f"Ошибка копирования настроек: {e}")

    @property
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) not in [10, 12] or not value.isdigit():
            raise argument_exception("ИНН должен содержать 10 или 12 цифр")
        self.__inn = value

    @property
    def bik(self) -> str:
        return self.__bik

    @bik.setter
    def bik(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 9 or not value.isdigit():
            raise argument_exception("БИК должен содержать 9 цифр")
        self.__bik = value

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 20 or not value.isdigit():
            raise argument_exception("Счет должен содержать 20 цифр")
        self.__account = value

    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 20 or not value.isdigit():
            raise argument_exception("Корреспондентский счет должен содержать 20 цифр")
        self.__correspondent_account = value

    @property
    def ownership(self) -> str:
        return self.__ownership

    @ownership.setter
    def ownership(self, value: str):
        validator.validate(value, str, 5)
        self.__ownership = value
