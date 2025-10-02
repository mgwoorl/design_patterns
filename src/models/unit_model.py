"""
Модель единицы измерения
"""

from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception

class unit_model(abstract_reference):
    __base_unit: 'unit_model' = None
    __conversion_factor: float = 1.0

    def __init__(self, name: str = "", conversion_factor: float = 1.0, base_unit: 'unit_model' = None):
        """
        Инициализация единицы измерения
        Args:
            name: наименование единицы
            conversion_factor: коэффициент пересчета
            base_unit: базовая единица измерения
        """
        super().__init__(name)
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit

    """ Базовая единица измерения """
    @property
    def base_unit(self):
        return self.__base_unit

    """ Устанавливает базовую единицу измерения """
    @base_unit.setter
    def base_unit(self, value):
        validator.validate(value, (unit_model, type(None)))
        self.__base_unit = value

    """ Коэффициент пересчета """
    @property
    def conversion_factor(self) -> float:
        return self.__conversion_factor

    """ Устанавливает коэффициент пересчета """
    @conversion_factor.setter
    def conversion_factor(self, value: float):
        validator.validate(value, (int, float), min_value = 0.0001)
        self.__conversion_factor = value
