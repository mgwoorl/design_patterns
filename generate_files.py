from src.start_service import start_service
from src.logics.factory_entities import factory_entities
from src.models.settings_model import settings_model, ResponseFormat
from src.reposity import reposity
import os

def generate_example_files():
    # Инициализация сервиса
    service = start_service()
    service.start()
    
    # Создание папки для результатов
    output_dir = "output_files"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Генерация файлов для каждого формата и типа данных
    settings = settings_model()
    factory = factory_entities(settings)
    
    entity_types = [
        (reposity.range_key(), "ranges"),
        (reposity.group_key(), "groups"), 
        (reposity.nomenclature_key(), "nomenclatures"),
        (reposity.receipt_key(), "receipts")
    ]
    
    formats = [ResponseFormat.CSV, ResponseFormat.MARKDOWN, ResponseFormat.JSON, ResponseFormat.XML]
    
    for entity_key, entity_name in entity_types:
        data = service.data.get(entity_key, [])
        if not data:
            continue
            
        for format_type in formats:
            settings.response_format = format_type
            formatter = factory.create_default(data)
            content = formatter.build(data)
            
            filename = f"{output_dir}/{entity_name}_{format_type.value}.{format_type.value}"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Generated: {filename}")

if __name__ == "__main__":
    generate_example_files()
