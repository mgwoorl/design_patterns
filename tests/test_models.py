import unittest
from src.models.company_model import company_model
from src.settings_manager import SettingsManager
from src.models.storage_model import storage_model
from src.models.unit_model import unit_model
from src.models.nomenclature_model import nomenclature_model
from src.models.nomenclature_group_model import nomenclature_group_model
import uuid

class test_models(unittest.TestCase):
    def test_empty_createmodel_companymodel(self):
        model = company_model()
        assert model.name == ""
        assert model.inn == ""
        assert model.account == ""
        assert model.correspondent_account == ""
        assert model.bik == ""
        assert model.ownership == ""

    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "Test"
        model.inn = "123456789012"
        model.account = "12345678901234567890"
        model.correspondent_account = "12345678901234567890"
        model.bik = "123456789"
        model.ownership = "OOO"

        assert model.name == "Test"
        assert model.inn == "123456789012"
        assert model.account == "12345678901234567890"
        assert model.correspondent_account == "12345678901234567890"
        assert model.bik == "123456789"
        assert model.ownership == "OOO"

    def test_convert_settings(self):
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
        manager.convert(data)

        s = manager.settings.company
        assert s.name == "Test Company"
        assert s.inn == "123456789012"
        assert s.account == "12345678901234567890"
        assert s.correspondent_account == "12345678901234567890"
        assert s.bik == "123456789"
        assert s.ownership == "OOO"

    def test_load_createmodel_companymodel(self):
        manager = SettingsManager()
        manager.load("settings.json")

        s = manager.settings.company
        assert s.name == "Ирис"
        assert s.inn == "123456789972"
        assert s.account == "12345678901234567890"
        assert s.correspondent_account == "12345678901234567890"
        assert s.bik == "123456789"
        assert s.ownership == "AO"

    def test_company_from_settings(self):
        manager = SettingsManager()
        manager.open("settings.json")
        company = company_model(settings=manager.settings)
        assert company.name == "Ирис"

    def test_unit_creation(self):
        gram = unit_model("грамм", 1)
        kg = unit_model("кг", 1000, gram)
        
        assert gram.name == "грамм"
        assert kg.name == "кг"
        assert kg.base_unit == gram

    def test_unit_conversion(self):
        gram = unit_model("грамм", 1)
        kg = unit_model("кг", 1000, gram)
        assert kg.conversion_factor == 1000

    def test_unit_without_base(self):
        unit = unit_model("штука", 1)
        assert unit.base_unit == None

    def test_nomenclature_creation(self):
        nomen = nomenclature_model("Товар")
        nomen.full_name = "Полное наименование товара"
        assert nomen.full_name == "Полное наименование товара"

    def test_nomenclature_full_name_length(self):
        nomen = nomenclature_model()
        long_name = "a" * 255
        nomen.full_name = long_name
        assert len(nomen.full_name) == 255

    def test_nomenclature_with_group_and_unit(self):
        group = nomenclature_group_model("Группа 1")
        unit = unit_model("шт", 1)
        nomen = nomenclature_model("Товар")
        nomen.group = group
        nomen.unit = unit
        
        assert nomen.group == group
        assert nomen.unit == unit

    def test_all_models_inheritance(self):
        company = company_model()
        unit = unit_model()
        nomen = nomenclature_model()
        group = nomenclature_group_model()
        storage = storage_model()
        
        assert isinstance(company, abstract_reference) == True
        assert isinstance(unit, abstract_reference) == True
        assert isinstance(nomen, abstract_reference) == True
        assert isinstance(group, abstract_reference) == True
        assert isinstance(storage, abstract_reference) == True

    def test_company_name_length(self):
        company = company_model()
        company.name = "a" * 50
        assert len(company.name) == 50

    def test_storage_model_creation(self):
        storage = storage_model("Склад 1")
        assert storage.name == "Склад 1"

    def test_nomenclature_group_creation(self):
        group = nomenclature_group_model("Основная группа")
        assert group.name == "Основная группа"

    def test_equals_storage_model_create(self):
        id = uuid.uuid4().hex
        storage1 = storage_model()
        storage1.id = id
        storage2 = storage_model()
        storage2.id = id
        assert storage1 == storage2

    def test_not_equals_storage_model(self):
        storage1 = storage_model()
        storage2 = storage_model()
        assert storage1 != storage2

if __name__ == "__main__":
    unittest.main()
