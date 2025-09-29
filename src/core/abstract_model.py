from abc import ABC
import uuid
from src.core.validator import validator

class abstract_reference(ABC):
    __id: str
    __name: str = ""

    def __init__(self, name: str = ""):
        self.__id = uuid.uuid4().hex
        self.name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, value: str):
        validator.validate(value, str)
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        validator.validate(value, str, 50)
        self.__name = value

    def __eq__(self, other) -> bool:
        if isinstance(other, abstract_reference):
            return self.__id == other.__id
        return False
