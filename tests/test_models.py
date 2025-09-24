import unittest
from src.models.company_model import CompanyModel
from src.settings_manager import SettingsManager

class test_models(unittest.TestCase):
    def test_empty_createmodel_companymodel(self):
        model = CompanyModel()
        assert model.name == ""
        assert model.inn == ""
        assert model.account == ""
        assert model.correspondent_account == ""
        assert model.bik == ""
        assert model.ownership == ""

    def test_notEmpty_createmodel_companymodel(self):
        model = CompanyModel()
        model.name = "Test"
        model.inn = "123456789012"
        model.account = "12345678901"
        model.correspondent_account = "12345678901"
        model.bik = "123456789"
        model.ownership = "OOO"

        assert model.name == "Test"
        assert model.inn == "123456789012"
        assert model.account == "12345678901"
        assert model.correspondent_account == "12345678901"
        assert model.bik == "123456789"
        assert model.ownership == "OOO"

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
        manager = SettingsManager()
        manager.convert(data)

        s = manager.settings.company
        assert s.name == "Test Company"
        assert s.inn == "123456789012"
        assert s.account == "12345678901"
        assert s.correspondent_account == "12345678901"
        assert s.bik == "123456789"
        assert s.ownership == "OOO"

    def test_load_createmodel_companymodel(self):
        manager = SettingsManager()
        manager.load("settings.json")

        s = manager.settings.company
        assert s.name == "Ирис"
        assert s.inn == "123456789972"
        assert s.account == "12345678901"
        assert s.correspondent_account == "12345678901"
        assert s.bik == "123456789"
        assert s.ownership == "AO"

    def test_load_from_other_dir(self):
        file_name = "D:/Шаблоны проектирования/data/other_dir_settings.json"
        manager = SettingsManager()
        result = manager.load(file_name)

        assert result is True
        s = manager.settings.company
        assert s.name == "OtherDirCompany"

    def test_invalid_inn_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.inn = "123"

    def test_invalid_bik_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.bik = "12"

    def test_invalid_account_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.account = "123"

    def test_invalid_corr_account_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.correspondent_account = "123"

    def test_invalid_ownership_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.ownership = "COMPANY"

    def test_empty_name_raises(self):
        model = CompanyModel()
        with self.assertRaises(ValueError):
            model.name = ""

    def test_none_name_raises(self):
        model = CompanyModel()
        with self.assertRaises(TypeError):
            model.name = None

if __name__ == "__main__":
    unittest.main()
