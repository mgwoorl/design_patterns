"""
Модель организации
"""

from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception
from src.models.settings import Settings

class company_model(abstract_reference):
    __inn: str = ""
    __bik: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __ownership: str = ""

    # ИНН : 12 симв
    # Счет 20 симв
    # Корреспондентский счет 20 симв
    # БИК 9 симв
    # Наименование
    # Вид собственности 5 симв

    def __init__(self, name: str = "", settings: Settings = None):
        """
        Инициализация модели компании
        Args:
            name: наименование компании
            settings: настройки для копирования данных
        """
        super().__init__(name)
        if settings and settings.company:
            self._copy_from_settings(settings.company)

    def _copy_from_settings(self, company_data):
        """
        Копирование данных из настроек
        Args:
            company_data: данные компании из настроек
        """
        # Проверяем наличие обязательных полей
        required_fields = ['name', 'inn', 'bik', 'account', 'correspondent_account', 'ownership']
        for field in required_fields:
            if not hasattr(company_data, field):
                raise argument_exception(f"Отсутствует обязательное поле: {field}")
        
        # Копируем данные
        self.name = company_data.name
        self.inn = company_data.inn
        self.bik = company_data.bik
        self.account = company_data.account
        self.correspondent_account = company_data.correspondent_account
        self.ownership = company_data.ownership

    """ Наименование """
    @property
    def name(self) -> str:
        return self.__name

    """ Устанавливает наименование """
    @name.setter
    def name(self, value: str):
        validator.validate(value, str)
        self.__name = value.strip()

    """ ИНН """
    @property
    def inn(self) -> str:
        return self.__inn
    
    """ Устанавливает ИНН """
    @inn.setter
    def inn(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) not in [10, 12] or not value.isdigit():
            raise argument_exception("ИНН должен содержать 10 или 12 цифр")
        self.__inn = value

    """ БИК """
    @property
    def bik(self) -> str:
        return self.__bik

    """ Устанавливает БИК """
    @bik.setter
    def bik(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 9 or not value.isdigit():
            raise argument_exception("БИК должен содержать 9 цифр")
        self.__bik = value

    """ Корреспондентский счет """
    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account
        
    """ Устанавливает корреспондентский счет """
    @correspondent_account.setter
    def correspondent_account(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 20 or not value.isdigit():
            raise argument_exception("Корреспондентский счет должен содержать 20 цифр")
        self.__correspondent_account = value

    """ Расчетный счет """
    @property
    def account(self) -> str:
        return self.__account
    
    """ Устанавливает расчетный счет """
    @account.setter
    def account(self, value: str):
        if isinstance(value, int):
            value = str(value)
        validator.validate(value, str)
        if len(value) != 20 or not value.isdigit():
            raise argument_exception("Счет должен содержать 20 цифр")
        self.__account = value

    """ Вид собственности """
    @property
    def ownership(self) -> str:
        return self.__ownership
    
    """ Устанавливает вид собственности """
    @ownership.setter
    def ownership(self, value: str):
        validator.validate(value, str, 5)
        self.__ownership = value.strip()
