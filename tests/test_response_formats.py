import unittest
from src.logics.response_csv import response_csv
from src.logics.response_markdown import response_markdown
from src.logics.response_json import response_json
from src.logics.response_xml import response_xml
from src.models.group_model import group_model
from src.models.range_model import range_model
from src.logics.factory_entities import factory_entities
from src.models.settings_model import settings_model, ResponseFormat

class test_response_formats(unittest.TestCase):

    def test_csv_format_creates_correct_structure(self):
        # Подготовка
        formatter = response_csv()
        data = [group_model.create("Test Group")]
        
        # Действие
        result = formatter.build(data)
        
        # Проверка
        self.assertIn("name", result)
        self.assertIn("unique_code", result)
        self.assertIn("Test Group", result)

    def test_markdown_format_creates_table(self):
        # Подготовка
        formatter = response_markdown()
        data = [group_model.create("Test Group")]
        
        # Действие
        result = formatter.build(data)
        
        # Проверка
        self.assertIn("| name |", result)
        self.assertIn("| --- |", result)
        self.assertIn("Test Group", result)

    def test_json_format_creates_valid_json(self):
        # Подготовка
        formatter = response_json()
        data = [group_model.create("Test Group")]
        
        # Действие
        result = formatter.build(data)
        
        # Проверка
        self.assertIn('"name": "Test Group"', result)
        # Проверка что это валидный JSON
        import json
        parsed = json.loads(result)
        self.assertEqual(len(parsed), 1)

    def test_xml_format_creates_valid_xml(self):
        # Подготовка
        formatter = response_xml()
        data = [group_model.create("Test Group")]
        
        # Действие
        result = formatter.build(data)
        
        # Проверка
        self.assertIn("<?xml", result)
        self.assertIn("<name>Test Group</name>", result)

    def test_factory_creates_correct_formatter_by_settings(self):
        # Подготовка
        settings = settings_model()
        settings.response_format = ResponseFormat.MARKDOWN
        factory = factory_entities(settings)
        
        # Действие
        formatter = factory.create_default([])
        
        # Проверка
        from src.logics.response_markdown import response_markdown
        self.assertIsInstance(formatter, response_markdown)
