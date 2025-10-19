"""
Модель номенклатуры
"""

from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception

class nomenclature_model(abstract_reference):
    __full_name: str = ""
    __group = None
    __unit = None

    def __init__(self, name: str = ""):
        """
        Инициализация номенклатуры
        Args:
            name: наименование номенклатуры
        """
        super().__init__(name)
        self.__full_name = name

    """ Полное наименование (строка до 255 символов) """
    @property
    def full_name(self) -> str:
        return self.__full_name

    """ Устанавливает полное наименование """
    @full_name.setter
    def full_name(self, value: str):
        validator.validate(value, str, 255)
        self.__full_name = value.strip()

    """ Группа номенклатуры """
    @property
    def group(self):
        return self.__group

    """ Устанавливает группу номенклатуры """
    @group.setter
    def group(self, value):
        # Простая проверка для None
        if value is not None:
            from src.models.nomenclature_group_model import nomenclature_group_model
            validator.validate(value, nomenclature_group_model)
        self.__group = value

    """ Единица измерения """
    @property
    def unit(self):
        return self.__unit

    """ Устанавливает единицу измерения """
    @unit.setter
    def unit(self, value):
        # Простая проверка для None
        if value is not None:
            from src.models.unit_model import unit_model
            validator.validate(value, unit_model)
        self.__unit = value
