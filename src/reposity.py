"""
Репозиторий данных
"""

from src.core.validator import validator, argument_exception

class reposity:
    __data = {}
    __keys = {
        'unit': "unit_model",
        'nomenclature': "nomenclature_model",
        'nomenclature_group': "nomenclature_group_model",
        'recipe': "recipe_model"
    }

    def __init__(self):
        """Инициализация репозитория"""
        for key in self.__keys.values():
            self.__data[key] = []

    @property
    def data(self):
        """Только для чтения"""
        return self.__data.copy()

    """
    Ключ для единиц измерений
    """
    @staticmethod
    def range_key():
        return "unit_model"

    """
    Ключ для номенклатуры
    """
    @staticmethod
    def nomenclature_key():
        return "nomenclature_model"

    """
    Ключ для групп номенклатуры
    """
    @staticmethod
    def nomenclature_group_key():
        return "nomenclature_group_model"

    """
    Ключ для рецептов
    """
    @staticmethod
    def recipe_key():
        return "recipe_model"

    def add_item(self, key: str, item):
        """
        Безопасное добавление элемента
        Args:
            key: Ключ коллекции
            item: Добавляемый элемент
        """
        validator.validate(key, str)
        if key not in self.__data:
            raise argument_exception(f"Некорректный ключ: {key}")
        self.__data[key].append(item)

    def get_items(self, key: str):
        """
        Безопасное получение коллекции
        Args:
            key: Ключ коллекции
        Returns:
            list: Копия коллекции
        """
        validator.validate(key, str)
        if key not in self.__data:
            raise argument_exception(f"Некорректный ключ: {key}")
        return self.__data[key].copy()
