"""
Модель склада
"""

from src.core.validator import validator
from src.core.abstract_model import abstract_reference

class storage_model(abstract_reference):
    
    def __init__(self, name: str = ""):
        """
        Инициализация модели склада
        Args:
            name: наименование склада
        """
        super().__init__(name)
