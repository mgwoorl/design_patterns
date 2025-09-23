class company_model:
    __name: str = ""
    __inn: str = ""
    __account: str = ""
    __correspondent_account: str = ""
    __bik: str = ""
    __ownership: str = ""

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        if value is None or not isinstance(value, str):
            raise TypeError("Наименование должно быть строкой")
        value = value.strip()
        if not value:
            raise ValueError("Наименование не может быть пустым")
        self.__name = value

    @property
    def inn(self) -> str:
        return self.__inn

    @inn.setter
    def inn(self, value: str | int):
        if isinstance(value, (str, int)):
            value = str(value).strip()
            if len(value) == 12 and value.isdigit():
                self.__inn = value
            else:
                raise ValueError("ИНН должен содержать 12 цифр")
        else:
            raise TypeError("ИНН должен быть строкой или числом")

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, value: str | int):
        if isinstance(value, (str, int)):
            value = str(value).strip()
            if len(value) == 11:
                self.__account = value
            else:
                raise ValueError("Счет должен содержать 11 цифр")
        else:
            raise TypeError("Счет должен быть строкой или числом")

    @property
    def correspondent_account(self) -> str:
        return self.__correspondent_account

    @correspondent_account.setter
    def correspondent_account(self, value: str | int):
        if isinstance(value, (str, int)):
            value = str(value).strip()
            if len(value) == 11 and value.isdigit():
                self.__correspondent_account = value
            else:
                raise ValueError("Корреспондентский счет должен содержать 11 цифр")
        else:
            raise TypeError("Корреспондентский счет должен быть строкой или числом")

    @property
    def bik(self) -> str:
        return self.__bik

    @bik.setter
    def bik(self, value: str | int):
        if isinstance(value, (str, int)):
            value = str(value).strip()
            if len(value) == 9 and value.isdigit():
                self.__bik = value
            else:
                raise ValueError("БИК должен содержать 9 цифр")
        else:
            raise TypeError("БИК должен быть строкой или числом")

    @property
    def ownership(self) -> str:
        return self.__ownership

    @ownership.setter
    def ownership(self, value: str):
        if isinstance(value, str):
            value = value.strip()
            if len(value) <= 5:
                self.__ownership = value
            else:
                raise ValueError("Вид собственности должен содержать не более 5 символов")
        else:
            raise TypeError("Вид собственности должен быть строкой")
