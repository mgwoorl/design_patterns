"""
Модель группы номенклатуры
"""

from src.core.abstract_model import abstract_reference


class nomenclature_group_model(abstract_reference):

    def __init__(self, name: str = ""):
        """
        Инициализация группы номенклатуры
        Args:
            name: наименование группы
        """
        super().__init__(name)
