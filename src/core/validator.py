class argument_exception(Exception):
    pass

class operation_exception(Exception):
    pass

class error_proxy:
    @staticmethod
    def handle_error(message: str):
        return message

class validator:
    @staticmethod
    def validate(value, expected_type, max_length=None):
        if value is None:
            raise argument_exception("Аргумент не может быть None")
        
        if not isinstance(value, expected_type):
            raise argument_exception(f"Ожидается тип {expected_type.__name__}")
        
        if isinstance(value, str):
            value = value.strip()
            if value == "":
                raise argument_exception("Строка не может быть пустой")
            
            if max_length and len(value) > max_length:
                raise argument_exception(f"Максимальная длина {max_length} символов")
        
        return True
