"""
Тесты для сервиса запуска и рецептов
"""

import unittest
from src.start_service import start_service
from src.reposity import reposity


class test_start_service(unittest.TestCase):

    def setUp(self):
        """Очистка данных перед каждым тестом"""
        # Получаем экземпляр сервиса
        self.service = start_service()
        
        # Полностью очищаем репозиторий
        self.service._start_service__repo = reposity()
        self.service._start_service__repo.data[reposity.range_key()] = []
        self.service._start_service__repo.data[reposity.nomenclature_key()] = []
        self.service._start_service__repo.data[reposity.nomenclature_group_key()] = []
        self.service._start_service__repo.data[reposity.recipe_key()] = []

    def test_start_service_creation(self):
        """Проверить создание сервиса запуска"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем

        # Действие
        service.create()

        # Проверки
        data = service.data()
        assert data is not None
        assert len(data) == 4

    def test_units_creation(self):
        """Проверить создание единиц измерения"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        units = service.data()[reposity.range_key()]

        # Проверки
        assert len(units) == 3

        unit_names = [unit.name for unit in units]
        assert "грамм" in unit_names
        assert "килограмм" in unit_names
        assert "штука" in unit_names

    def test_groups_creation(self):
        """Проверить создание групп номенклатуры"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        groups = service.data()[reposity.nomenclature_group_key()]

        # Проверки
        assert len(groups) == 4

        group_names = [group.name for group in groups]
        assert "Мука и крупы" in group_names
        assert "Сладости" in group_names
        assert "Молочные продукты" in group_names
        assert "Прочее" in group_names

    def test_nomenclature_creation(self):
        """Проверить создание номенклатуры"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        nomenclature = service.data()[reposity.nomenclature_key()]

        # Проверки
        assert len(nomenclature) == 6

        nomen_names = [nomen.name for nomen in nomenclature]
        assert "Пшеничная мука" in nomen_names
        assert "Мед натуральный" in nomen_names
        assert "Сахарный песок" in nomen_names
        assert "Сливочное масло" in nomen_names
        assert "Яйца куриные" in nomen_names
        assert "Сода пищевая" in nomen_names

    def test_recipes_creation(self):
        """Проверить создание рецептов"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]

        # Проверки
        assert len(recipes) == 1

        recipe = recipes[0]
        assert recipe.name == "Медовое печенье"
        assert recipe.description == "Ароматное медовое печенье"
        assert recipe.cooking_time == "45 мин"
        assert recipe.portions == "25-30 штук"
        assert len(recipe.ingredients) == 6
        assert len(recipe.steps) == 14

    def test_recipe_ingredients(self):
        """Проверить ингредиенты рецепта"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]
        recipe = recipes[0]

        # Проверки
        assert recipe.name == "Медовое печенье"

        # Проверяем наличие основных ингредиентов
        ingredients = recipe.ingredients
        assert "Пшеничная мука - 400 гр" in ingredients
        assert "Мед натуральный - 100 гр" in ingredients
        assert "Сахарный песок - 150 гр" in ingredients
        assert "Сливочное масло - 100 гр" in ingredients
        assert "Яйца куриные - 2 шт" in ingredients
        assert "Сода пищевая - 5 гр" in ingredients

    def test_recipe_steps(self):
        """Проверить шаги приготовления"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]
        recipe = recipes[0]

        # Проверки
        steps = recipe.steps
        assert len(steps) == 14
        assert "Духовку разогрейте до 180°C" in steps[0]
        assert "дайте полностью остыть на решетке" in steps[-1]

    def test_singleton_pattern(self):
        """Проверить паттерн Singleton"""
        # Действие
        service1 = start_service()
        service2 = start_service()

        # Проверки
        assert service1 is service2

    def test_data_structure(self):
        """Проверить структуру данных"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        data = service.data()

        # Проверки
        assert reposity.range_key() in data
        assert reposity.nomenclature_key() in data
        assert reposity.nomenclature_group_key() in data
        assert reposity.recipe_key() in data

    def test_recipe_properties(self):
        """Проверить свойства рецепта"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]
        recipe = recipes[0]

        # Проверки
        assert recipe.description == "Ароматное медовое печенье"  # ← ИСПРАВЛЕНО: печенье
        assert recipe.cooking_time == "45 мин"
        assert recipe.portions == "25-30 штук"

    def test_ingredients_count(self):
        """Проверить количество ингредиентов"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]
        recipe = recipes[0]

        # Проверки
        assert len(recipe.ingredients) == 6

    def test_steps_count(self):
        """Проверить количество шагов приготовления"""
        # Подготовка
        service = start_service()
        service._start_service__repo = reposity()  # Очищаем
        service.create()

        # Действие
        recipes = service.data()[reposity.recipe_key()]
        recipe = recipes[0]

        # Проверки
        assert len(recipe.steps) == 14


if __name__ == '__main__':
    unittest.main()
