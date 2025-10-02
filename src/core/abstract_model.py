"""
Базовый абстрактный класс для справочных сущностей
"""

from abc import ABC
import uuid
from src.core.validator import validator, argument_exception

"""
Базовый абстрактный класс модели
Содержит уникальный код и перегрузку сравнения
"""
class abstract_reference(ABC):

    __id: str
    __name: str = ""

    def __init__(self, name: str = "") -> None:
        """
        Инициализация справочной модели
        Args:
            name: наименование (строка до 50 символов)
        """
        super().__init__()
        self.__id = uuid.uuid4().hex
        if name:
            self.name = name

    """ Уникальный код модели """
    @property
    def id(self) -> str:
        return self.__id

    """ Устанавливает уникальный код """
    @id.setter
    def id(self, value: str):
        validator.validate(value, str)
        self.__id = value.strip()

    """ Наименование (строка до 50 символов) """
    @property
    def name(self) -> str:
        return self.__name

    """ Устанавливает наименование с проверкой длины (<=50) """
    @name.setter
    def name(self, value: str):
        try:
            validator.validate(value, str, 50)
        except argument_exception as ex:
            raise
        self.__name = value.strip()

    """ Перегрузка сравнения по уникальному коду """
    def __eq__(self, other) -> bool:
        if isinstance(other, abstract_reference):
            return self.__id == other.__id
        return False
