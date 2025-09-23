import os
import json
import unittest
from src.models.company_model import company_model
from src.settings_manager import settings_manager

class test_models(unittest.TestCase):
    def test_empty_createmodel_companymodel(self):
        model = company_model()
        model.name == ""
        model.inn == ""
        model.account == ""
        model.correspondent_account == ""
        model.bik == ""
        model.ownership == ""

    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()
        model.name = "Test"
        model.inn = "123456789012"
        model.account = "12345678901"
        model.correspondent_account = "12345678901"
        model.bik = "123456789"
        model.ownership = "OOO"

        model.name == "Test"
        model.inn == "123456789012"
        model.account == "12345678901"
        model.correspondent_account == "12345678901"
        model.bik == "123456789"
        model.ownership == "OOO"

    # Конвертация настроек из словаря
    def test_convert_settings(self):
        data = {
            "company": {
                "name": "Test Company",
                "inn": "123456789012",
                "account": "12345678901",
                "correspondent_account": "12345678901",
                "bik": "123456789",
                "ownership": "OOO"
            }
        }
        manager = settings_manager()
        manager.convert(data)

        s = manager.settings.company
        s.name == "Test Company"
        s.inn == "123456789012"
        s.account == "12345678901"
        s.correspondent_account == "12345678901"
        s.bik == "123456789"
        s.ownership == "OOO"

    # Загрузка настроек через существующий файл
    def test_load_createmodel_companymodel(self):
        file_name = '../settings.json'
        manager = settings_manager()
        manager.file_name = file_name
        result = manager.load()

        result == True

        manager.settings.company.name == "Ирис"
        manager.settings.company.inn == "123456789012"
        manager.settings.company.account == "12345678901"
        manager.settings.company.correspondent_account == "12345678901"
        manager.settings.company.bik == "123456789"
        manager.settings.company.ownership == "AO"

    # Загрузка настроек из другой директории
    def test_load_from_other_dir(self):
        file_name = "D:/Шаблоны проектирования/data/other_dir_settings.json"

        manager = settings_manager()
        manager.file_name = file_name
        result = manager.load()

        result == True
        manager.settings.company.name == "OtherDirCompany"

    def test_invalid_inn_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.inn = "123"

    def test_invalid_bik_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.bik = "12"

    def test_invalid_account_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.account = "123"

    def test_invalid_corr_account_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.correspondent_account = "123"

    def test_invalid_ownership_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.ownership = "COMPANY"

    def test_empty_name_raises(self):
        model = company_model()
        with self.assertRaises(ValueError):
            model.name = ""

    def test_none_name_raises(self):
        model = company_model()
        with self.assertRaises(TypeError):
            model.name = None

    def test_default_settings(self):
        manager = settings_manager()

        s = manager.settings.company

        assert s.name == "Default"
        assert s.inn == ""
        assert s.account == ""
        assert s.correspondent_account == ""
        assert s.bik == ""
        assert s.ownership == ""

if __name__ == "__main__":
    unittest.main()
