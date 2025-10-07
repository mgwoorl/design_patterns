"""
Модель рецепта
"""

from src.core.abstract_model import abstract_reference
from src.core.validator import validator, argument_exception

class recipe_model(abstract_reference):
    """
    Модель рецепта
    """
    __description: str = ""
    __cooking_time: str = ""
    __portions: str = ""
    __ingredients: list = None
    __steps: list = None

    def __init__(self, name: str = ""):
        super().__init__(name)
        self.__ingredients = []
        self.__steps = []

    """ Описание рецепта """
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, value: str):
        validator.validate(value, str, 500)
        self.__description = value.strip()

    """ Время приготовления """
    @property
    def cooking_time(self) -> str:
        return self.__cooking_time

    @cooking_time.setter
    def cooking_time(self, value: str):
        validator.validate(value, str, 50)
        self.__cooking_time = value.strip()

    """ Количество порций """
    @property
    def portions(self) -> str:
        return self.__portions

    @portions.setter
    def portions(self, value: str):
        validator.validate(value, str, 20)
        self.__portions = value.strip()

    """ Ингредиенты """
    @property
    def ingredients(self) -> list:
        return self.__ingredients

    def add_ingredient(self, ingredient: str):
        validator.validate(ingredient, str, 100)
        self.__ingredients.append(ingredient.strip())

    """ Шаги приготовления """
    @property
    def steps(self) -> list:
        return self.__steps

    def add_step(self, step: str):
        validator.validate(step, str, 1000)
        self.__steps.append(step.strip())
