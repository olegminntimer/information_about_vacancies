from typing import Any

from src.utils import range_bounds_check


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = "name", "salary", "url", "requirement"

    def __init__(self, name: str, salary: str, url: str, requirement: str):
        """Конструктор класса Vacancy"""
        self.name = name
        self.salary = self.__valid_salary(salary)
        self.url = url
        self.requirement = requirement

    @classmethod
    def __valid_salary(cls, salary: str) -> int | dict:
        """Приватный метод проверки диапазона зарплаты"""
        limits = range_bounds_check(salary)
        if limits:
            return {"from": limits[0], "to": limits[1], "currency": "RUR"}
        else:
            return 0

    @classmethod
    def __verify_data(cls, some) -> Any:
        """Валидация при сравнении вакансий"""
        if not isinstance(some, Vacancy):
            raise TypeError("Операнд должен иметь тип Vacancy")

        if isinstance(some.salary, dict):
            return some.salary["from"]
        else:
            return 0

    def __eq__(self, other) -> bool:
        """Магический метод проверки равенства"""
        return self.__verify_data(self) == self.__verify_data(other)

    def __lt__(self, other) -> bool:
        """Магический метод проверки, что операнд слева меньше операнда справа"""
        return self.__verify_data(self) < self.__verify_data(other)

    def __le__(self, other) -> bool:
        """Магический метод проверки, что операнд слева меньше или равен операнду справа"""
        return self.__verify_data(self) <= self.__verify_data(other)

    def to_file(self) -> dict:
        """Метод конвертации вакансии в словарь для добавления в файл"""
        return {"name": self.name, "salary": self.salary, "alternate_url": self.url, "requirement": self.requirement}


# if __name__ == "__main__":
#     vacancy1 = Vacancy("Геофизик", 0, "<https://hh.ru/vacancy/123456>",
#                        "Требования: опыт работы от 1 года...")
#     print(vacancy1.to_file())
#     vacancy2 = Vacancy("Геолог", "2aasd21sfgsg", "<https://hh.ru/vacancy/123457>",
#                        "Требования: без опыта...")
#     print(vacancy2.to_file())
#     vacancy3 = Vacancy("Ведущий геолог", "150000 руб", "<https://hh.ru/vacancy/123458>",
#                        "Требования: опыта 3 года...")
#     print(vacancy3.to_file())
#     print(vacancy1 == vacancy2)
#     print(vacancy2 > vacancy3)
#     print(vacancy1 > vacancy3)
