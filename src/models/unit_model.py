
from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception

class unit_model(abstract_reference):
    __base_unit: 'unit_model' = None
    __conversion_factor: float = 1.0

    def __init__(self, name: str = "", conversion_factor: float = 1.0, base_unit: 'unit_model' = None):
        super().__init__(name)
        self.conversion_factor = conversion_factor
        self.base_unit = base_unit

    @property
    def base_unit(self):
        return self.__base_unit

    @base_unit.setter
    def base_unit(self, value):
        if value is not None and not isinstance(value, unit_model):
            raise argument_exception("Базовая единица должна быть unit_model")
        self.__base_unit = value

    @property
    def conversion_factor(self) -> float:
        return self.__conversion_factor

    @conversion_factor.setter
    def conversion_factor(self, value: float):
        validator.validate(value, (int, float))
        if value <= 0:
            raise argument_exception("Коэффициент должен быть > 0")
        self.__conversion_factor = value
