"""
Исключение при проверке аргумента
"""


class argument_exception(Exception):
    pass


"""
Исключение при выполнении бизнес операции
"""


class operation_exception(Exception):
    pass


"""
Прокси для обработки ошибок
"""


class error_proxy:

    @staticmethod
    def handle_error(message: str):
        """
            Обработка ошибки
        Args:
            message (str): Сообщение об ошибке
        Returns:
            str: Сообщение об ошибке
        """
        return message


"""
Набор проверок данных
"""


class validator:

    @staticmethod
    def validate(value, type_, len_=None, min_value=None):
        """
            Валидация аргумента по типу и длине
        Args:
            value (any): Аргумент
            type_ (object): Ожидаемый тип
            len_ (int): Максимальная длина
            min_value (any): Минимальное значение
        Raises:
            argument_exception: Некорректный тип
            argument_exception: Неулевая длина
            argument_exception: Некорректная длина аргумента
            argument_exception: Некорректное значение
        Returns:
            True или Exception
        """

        if value is None:
            raise argument_exception("Пустой аргумент")

        # Проверка типа
        if not isinstance(value, type_):
            raise argument_exception(f"Некорректный тип!\nОжидается {type_}. Текущий тип {type(value)}")

        # Проверка аргумента
        if len(str(value).strip()) == 0:
            raise argument_exception("Пустой аргумент")

        if len_ is not None and len(str(value).strip()) > len_:
            raise argument_exception("Некорректная длина аргумента")

        if min_value is not None and value < min_value:
            raise argument_exception(f"Некорректное значение. Должно быть не менее {min_value}")

        return True
