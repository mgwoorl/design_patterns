"""
Тесты для всех моделей проекта
"""

import unittest
import uuid
import os


class test_models(unittest.TestCase):

    # Проверить создание пустой модели компании
    # Данные после создания должны быть пустыми
    def test_empty_createmodel_companymodel(self):
        # Подготовка
        from src.models.company_model import company_model
        model = company_model()

        # Действие
        model.name = "Test"
        model.inn = "1234567890" 
        model.account = "12345678901234567890"  
        model.correspondent_account = "12345678901234567890"  
        model.bik = "123456789"  
        model.ownership = "OOO" 

        # Проверки
        assert model.name == "Test"
        assert model.inn == "1234567890"
        assert model.account == "12345678901234567890"
        assert model.correspondent_account == "12345678901234567890"
        assert model.bik == "123456789"
        assert model.ownership == "OOO"

    # Проверить создание модели компании с данными
    # Данные меняем. Данные должны быть установлены
    def test_notEmpty_createmodel_companymodel(self):
        # Подготовка
        from src.models.company_model import company_model
        model = company_model()

        # Действие
        model.name = "Test"
        model.inn = "123456789012"
        model.account = "12345678901234567890"
        model.correspondent_account = "12345678901234567890"
        model.bik = "123456789"
        model.ownership = "OOO"

        # Проверки
        assert model.name == "Test"
        assert model.inn == "123456789012"
        assert model.account == "12345678901234567890"
        assert model.correspondent_account == "12345678901234567890"
        assert model.bik == "123456789"
        assert model.ownership == "OOO"

    # Проверить конвертацию настроек
    # Данные загружаем через словарь
    def test_convert_settings(self):
        # Подготовка
        from src.settings_manager import SettingsManager
        data = {
            "company": {
                "name": "Test Company",
                "inn": "123456789012",
                "account": "12345678901234567890",
                "correspondent_account": "12345678901234567890",
                "bik": "123456789",
                "ownership": "OOO"
            }
        }
        manager = SettingsManager()

        # Действие
        manager.convert(data)

        # Проверки
        s = manager.settings.company
        assert s.name == "Test Company"
        assert s.inn == "123456789012"
        assert s.account == "12345678901234567890"
        assert s.correspondent_account == "12345678901234567890"
        assert s.bik == "123456789"
        assert s.ownership == "OOO"

    # Проверить загрузку настроек из файла
    # Данные загружаем через json настройки
    def test_load_createmodel_companymodel(self):
        # Подготовка
        from src.settings_manager import SettingsManager
        manager = SettingsManager()

        # Создаем временный файл настроек для теста
        test_settings = {
            "company": {
                "name": "Ирис",
                "inn": "123456789972",
                "account": "12345678901234567890",
                "correspondent_account": "12345678901234567890",
                "bik": "123456789",
                "ownership": "AO"
            }
        }

        import json
        with open("test_settings.json", "w", encoding="utf-8") as f:
            json.dump(test_settings, f, ensure_ascii=False, indent=4)

        # Действие
        manager.load("test_settings.json")

        # Проверки
        s = manager.settings.company
        assert s.name == "Ирис"
        assert s.inn == "123456789972"
        assert s.account == "12345678901234567890"
        assert s.correspondent_account == "12345678901234567890"
        assert s.bik == "123456789"
        assert s.ownership == "AO"

        # Удаляем временный файл
        os.remove("test_settings.json")

    # Проверить создание компании из настроек
    # Данные копируются из загруженных настроек
    def test_company_from_settings(self):
        # Подготовка
        from src.settings_manager import SettingsManager
        from src.models.company_model import company_model

        # Создаем временный файл настроек для теста
        test_settings = {
            "company": {
                "name": "Ирис",
                "inn": "123456789972",
                "account": "12345678901234567890",
                "correspondent_account": "12345678901234567890",
                "bik": "123456789",
                "ownership": "AO"
            }
        }

        import json
        with open("test_settings.json", "w", encoding="utf-8") as f:
            json.dump(test_settings, f, ensure_ascii=False, indent=4)

        manager = SettingsManager()
        manager.load("test_settings.json")

        # Действие
        company = company_model(settings=manager.settings)

        # Проверки
        assert company.name == "Ирис"

        # Удаляем временный файл
        os.remove("test_settings.json")

    # Проверить создание единиц измерения
    # Создаем базовую и производную единицы
    def test_unit_creation(self):
        # Подготовка
        from src.models.unit_model import unit_model

        # Действие
        gram = unit_model("грамм", 1)
        kg = unit_model("кг", 1000)

        # Проверки
        assert gram.name == "грамм"
        assert kg.name == "кг"
        assert kg.base_unit == None

    # Проверить коэффициент пересчета единиц измерения
    # Коэффициент должен быть установлен корректно
    def test_unit_conversion(self):
        # Подготовка
        from src.models.unit_model import unit_model
        gram = unit_model("грамм", 1)

        # Действие
        kg = unit_model("кг", 1000)

        # Проверки
        assert kg.conversion_factor == 1000

    # Проверить создание единицы измерения без базовой единицы
    # Базовая единица должна быть None
    def test_unit_without_base(self):
        # Подготовка
        from src.models.unit_model import unit_model

        # Действие
        unit = unit_model("штука", 1)

        # Проверки
        assert unit.base_unit == None

    # Проверить создание номенклатуры
    # Полное наименование должно устанавливаться
    def test_nomenclature_creation(self):
        # Подготовка
        from src.models.nomenclature_model import nomenclature_model
        nomen = nomenclature_model("Товар")

        # Действие
        nomen.full_name = "Полное наименование товара"

        # Проверки
        assert nomen.full_name == "Полное наименование товара"

    # Проверить максимальную длину полного наименования номенклатуры
    # Длина должна быть 255 символов
    def test_nomenclature_full_name_length(self):
        # Подготовка
        from src.models.nomenclature_model import nomenclature_model
        nomen = nomenclature_model()
        long_name = "a" * 255

        # Действие
        nomen.full_name = long_name

        # Проверки
        assert len(nomen.full_name) == 255

    # Проверить наследование всех моделей от abstract_reference
    # Все модели должны наследоваться от базового класса
    def test_all_models_inheritance(self):
        # Подготовка
        from src.core.abstract_model import abstract_reference
        from src.models.company_model import company_model
        from src.models.unit_model import unit_model
        from src.models.nomenclature_model import nomenclature_model
        from src.models.nomenclature_group_model import nomenclature_group_model
        from src.models.storage_model import storage_model

        company = company_model()
        unit = unit_model()
        nomen = nomenclature_model()
        group = nomenclature_group_model()
        storage = storage_model()

        # Действие

        # Проверки
        assert isinstance(company, abstract_reference) == True
        assert isinstance(unit, abstract_reference) == True
        assert isinstance(nomen, abstract_reference) == True
        assert isinstance(group, abstract_reference) == True
        assert isinstance(storage, abstract_reference) == True

    # Проверка на сравнение двух по значению одинаковых моделей
    def test_equals_storage_model_create(self):
        # Подготовка
        from src.models.storage_model import storage_model
        id = uuid.uuid4().hex
        storage1 = storage_model()
        storage1.id = id
        storage2 = storage_model()
        storage2.id = id

        # Действие

        # Проверки
        assert storage1 == storage2


if __name__ == '__main__':
    unittest.main()
