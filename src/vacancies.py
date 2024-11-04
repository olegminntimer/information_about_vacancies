


class Vacancy():
    """Класс для работы с вакансиями"""
    __slots__ = 'id', 'name', 'url', 'salary', 'requirement'

    def __init__(self, id: str, name: str, url: str, salary: [str|None], requirement: str):
        """Конструктор класса Vacancy"""
        self.id = id
        self.name = name
        self.url = url
        self.salary = self.__valid_salary(salary)
        self.requirement = requirement

    @classmethod
    def __valid_salary(cls, salary):
        """Приватный метод проверки зарплаты"""
        if not salary:
            return "Зарплата не указана"
        else:
            return salary

    @classmethod
    def __verify_data(cls, some):
        """Валидация при сравнении вакансий"""
        if not isinstance(some, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")

        if some.salary:
            if "-" in some.salary.split()[0]:
                return int(some.salary.split()[0].split("-")[0])
            else:
                return 0


    def __eq__(self, other):
        """Магический метод проверки равенства"""
        return self.__verify_data(self) == self.__verify_data(other)

    def __lt__(self, other):
        """Магический метод проверки, что операнд слева меньше операнда справа """
        return self.__verify_data(self) < self.__verify_data(other)

    def __le__(self, other):
        """Магический метод проверки, что операнд слева меньше или равен операнду справа """
        return self.__verify_data(self) <= self.__verify_data(other)


if __name__ == "__main__":
    vacancy1 = Vacancy("108971116", "Python Developer", "<https://hh.ru/vacancy/123456>", None,
                      "Требования: опыт работы от 3 лет...")
    print(f"For {vacancy1.name} salary {vacancy1.salary}")
    vacancy2 = Vacancy("109680570", "Python Developer2", "<https://hh.ru/vacancy/123456>", "100000-150000 руб",
                      "Требования: опыт работы от 3 лет...")
    print(f"For {vacancy2.name} salary {vacancy2.salary}")

    print(vacancy1 <= vacancy2)
