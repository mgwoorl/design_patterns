import unittest
from src.models.company_model import company_model
from src.settings_manager import settings_manager

class test_models(unittest.TestCase):
    def test_empty_createmodel_companymodel(self):
        model = company_model()

        assert model.name == ""

    def test_notEmpty_createmodel_companymodel(self):
        model = company_model()

        model.name = "test"

        assert model.name != ""

    def test_load_createmodel_companymodel(self):
       file_name = "D:\Шаблоны проектирования\design_patterns\settings.json"

       manager = settings_manager()
       manager.file_name = file_name

       result = manager.load()

       assert result == True

    def test_loadCombo_createmodel_companymodel(self):
        file_name = "D:\Шаблоны проектирования\design_patterns\settings.json"

        manager1 = settings_manager()
        manager1.file_name = file_name
        manager2 = settings_manager()

        manager1.load()

        assert manager1.company == manager2.company
  
if __name__ == '__main__':
    unittest.main()   
