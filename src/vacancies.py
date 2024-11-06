import re
from typing import Any


class Vacancy():
    """Класс для работы с вакансиями"""
    __slots__ = 'name', 'salary', 'url', 'requirement'

    def __init__(self, name: str, salary: str, url: str, requirement: str) -> None:
        """Конструктор класса Vacancy"""
        self.name = name
        self.salary = self.__valid_salary(salary)
        self.url = url
        self.requirement = requirement

    @classmethod
    def __valid_salary(cls, salary: Any) -> int | dict:
        """Приватный метод проверки диапазона зарплаты"""
        if salary:
            left_limit = None
            right_limit = 0
            for i in re.split('[- ]', salary):
                if not isinstance(left_limit, int):
                    try:
                        left_limit = int(i)
                    except ValueError:
                        left_limit = 0
                        continue
                else:
                    if right_limit == 0:
                        try:
                            right_limit = int(i)
                            break
                        except ValueError:
                            continue
            if (left_limit == 0) and (right_limit == 0):
                return 0
            else:
                return {"from": left_limit, "to": right_limit, "currency": "RUB"}
        else:
            return 0

    @classmethod
    def __verify_data(cls, some) -> int:
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
        """Магический метод проверки, что операнд слева меньше операнда справа """
        return self.__verify_data(self) < self.__verify_data(other)

    def __le__(self, other) -> bool:
        """Магический метод проверки, что операнд слева меньше или равен операнду справа """
        return self.__verify_data(self) <= self.__verify_data(other)

    def to_file(self) -> dict:
        """Метод конвертации вакансии в словарь для добавления в файл"""
        return {"name": self.name, "salary": self.salary, "alternate_url": self.url, "requirement": self.requirement}


if __name__ == "__main__":
    vacancy1 = Vacancy("Геофизик", None, "<https://hh.ru/vacancy/123456>",
                       "Требования: опыт работы от 1 года...")
    print(f"For {vacancy1.name} salary {vacancy1.salary}")
    print(vacancy1.to_file())
    vacancy2 = Vacancy("Геолог", "a 21", "<https://hh.ru/vacancy/123457>",
                       "Требования: без опыта...")
    print(f"For {vacancy2.name} salary {vacancy2.salary}")
    print(vacancy2.to_file())
    vacancy3 = Vacancy("Ведущий геолог", "150000 руб", "<https://hh.ru/vacancy/123458>",
                       "Требования: опыта 3 года...")
    print(f"For {vacancy3.name} salary {vacancy3.salary}")
    print(vacancy3.to_file())
    print(vacancy1 <= vacancy2)
