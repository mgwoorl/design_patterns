
from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception

class nomenclature_model(abstract_reference):
    __full_name: str = ""
    __group: 'nomenclature_group_model' = None
    __unit: 'unit_model' = None

    def __init__(self, name: str = ""):
        super().__init__(name)
        self.__full_name = name

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, value: str):
        validator.validate(value, str, 255)
        self.__full_name = value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        if value is not None and not isinstance(value, nomenclature_group_model):
            raise argument_exception("Группа должна быть nomenclature_group_model")
        self.__group = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        if value is not None and not isinstance(value, unit_model):
            raise argument_exception("Единица должна быть unit_model")
        self.__unit = value
