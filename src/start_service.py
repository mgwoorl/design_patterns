from src.reposity import reposity
from src.models.unit_model import unit_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
from src.models.recepie_model import recipe_model


class start_service:
    __repo: reposity = reposity()

    def __init__(self):
        self.__repo.data[reposity.range_key()] = []
        self.__repo.data[reposity.nomenclature_key()] = []
        self.__repo.data[reposity.nomenclature_group_key()] = []
        self.__repo.data[reposity.recipe_key()] = []

    # Singletone
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(start_service, cls).__new__(cls)
        return cls.instance

    def __default_create_units(self):
        """Создание единиц измерения"""
        self.__repo.data[reposity.range_key()].append(unit_model("грамм", 1))
        self.__repo.data[reposity.range_key()].append(unit_model("килограмм", 1000))
        self.__repo.data[reposity.range_key()].append(unit_model("штука", 1))

    def __default_create_groups(self):
        """Создание групп номенклатуры"""
        groups = [
            "Мука и крупы",
            "Сладости",
            "Молочные продукты",
            "Прочее"
        ]

        for group_name in groups:
            group = nomenclature_group_model(group_name)
            self.__repo.data[reposity.nomenclature_group_key()].append(group)

    def __default_create_nomenclature(self):
        """Создание номенклатуры"""
        # Находим группы
        flour_group = self.__find_group("Мука и крупы")
        sweets_group = self.__find_group("Сладости")
        other_group = self.__find_group("Прочее")

        # Находим единицы измерения
        gram_unit = self.__find_unit("грамм")
        piece_unit = self.__find_unit("штука")

        # Создаем номенклатуру
        items = [
            {"name": "Пшеничная мука", "group": flour_group, "unit": gram_unit},
            {"name": "Мед натуральный", "group": sweets_group, "unit": gram_unit},
            {"name": "Сахарный песок", "group": sweets_group, "unit": gram_unit},
            {"name": "Сливочное масло", "group": sweets_group, "unit": gram_unit},
            {"name": "Яйца куриные", "group": other_group, "unit": piece_unit},
            {"name": "Сода пищевая", "group": other_group, "unit": gram_unit}
        ]

        for item in items:
            nomen = nomenclature_model(item["name"])
            nomen.group = item["group"]
            nomen.unit = item["unit"]
            self.__repo.data[reposity.nomenclature_key()].append(nomen)

    def __find_group(self, group_name):
        """Поиск группы по имени"""
        for group in self.__repo.data[reposity.nomenclature_group_key()]:
            if group.name == group_name:
                return group
        return None

    def __find_unit(self, unit_name):
        """Поиск единицы измерения по имени"""
        for unit in self.__repo.data[reposity.range_key()]:
            if unit.name == unit_name:
                return unit
        return None

    def create_receipts(self):
        """Фабричный метод для создания рецептов"""
        # Создаем рецепт медового печенья
        honey_cookies = recipe_model("Медовое печенье")
        honey_cookies.description = "Ароматное медовое печенье"
        honey_cookies.cooking_time = "45 мин"
        honey_cookies.portions = "25-30 штук"

        # Добавляем ингредиенты как строки
        honey_cookies.add_ingredient("Пшеничная мука - 400 гр")
        honey_cookies.add_ingredient("Мед натуральный - 100 гр")
        honey_cookies.add_ingredient("Сахарный песок - 150 гр")
        honey_cookies.add_ingredient("Сливочное масло - 100 гр")
        honey_cookies.add_ingredient("Яйца куриные - 2 шт")
        honey_cookies.add_ingredient("Сода пищевая - 5 гр")

        # Добавляем шаги приготовления
        steps = [
            "Подготовьте все необходимые ингредиенты. Масло достаньте заранее, чтобы оно стало мягким. Духовку разогрейте до 180°C.",
            "В глубокой миске взбейте размягченное сливочное масло с сахарным песком до легкой пышной массы.",
            "Добавьте к массе яйца по одному, продолжая взбивать после каждого добавления.",
            "В отдельной посуде смешайте мед с пищевой содой. Тщательно перемешайте - смесь немного посветлеет.",
            "Соедините медовую смесь с масляно-яичной массой. Аккуратно перемешайте до однородности.",
            "В отдельной миске просейте муку и добавьте щепотку соли. Тщательно перемешайте.",
            "Постепенно добавляйте мучную смесь к жидкой основе, постоянно помешивая.",
            "Замесите мягкое, эластичное тесто. Оно не должно липнуть к рукам.",
            "Готовое тесто заверните в пищевую пленку и отправьте в холодильник на 30 минут.",
            "Достаньте тесто из холодильника. Раскатайте его толщиной около 0.5-0.7 см.",
            "Используйте формочки для печенья или стакан, чтобы вырезать кружки диаметром 5-6 см.",
            "Противень застелите бумагой для выпечки. Разложите печенье на расстоянии 2-3 см друг от друга.",
            "Выпекайте в разогретой до 180°C духовке 10-12 минут до золотистого цвета.",
            "Готовое печенье достаньте из духовки и дайте полностью остыть на решетке."
        ]

        for step in steps:
            honey_cookies.add_step(step)

        self.__repo.data[reposity.recipe_key()].append(honey_cookies)

    def create(self):
        """
        Основной метод для генерации эталонных данных
        """
        self.__default_create_units()
        self.__default_create_groups()
        self.__default_create_nomenclature()
        self.create_receipts()

    def data(self):
        """Стартовый набор данных"""
        return self.__repo.data
