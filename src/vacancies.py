import re


class Vacancy():
    """Класс для работы с вакансиями"""
    __slots__ = 'name', 'url', 'salary', 'requirement'

    def __init__(self, name: str, url: str, salary: [str | None], requirement: str):
        """Конструктор класса Vacancy"""
        self.name = name
        self.url = url
        self.salary = self.__valid_salary(salary)
        self.requirement = requirement

    def __str__(self) -> str:
        """Магический метод для строкового отображения вакансии в виде словаря"""
        if self.salary != 0:
            salary_list = re.split('[- ]', self.salary)
            if len(salary_list) == 3:
                salary_ = {"from": int(salary_list[0]), "to": int(salary_list[1]), "currency": salary_list[2],
                           "gross": False}
            elif len(salary_list) == 2:
                salary_ = {"from": int(salary_list[0]), "to": None, "currency": salary_list[1], "gross": False}
        else:
            salary_ = None
        return (f'{{"id": "", "premium": False, "name": {self.name}, "department": None, "has_test": False, \
"response_letter_required": False, "area": {{"id": "", "name": None, "url": None}}, "salary": {salary_}, \
"type": {{"id": "open", "name": "Открытая"}}, "address": {{"city": "", "street": "", "building": "", \
"lat": None, "lng": None, "description": None, "raw": "", "metro": None, "metro_stations": [], "id": ""}}, \
"response_url": None, "sort_point_distance": None, "published_at": "", "created_at": "", "archived": False, \
"apply_alternate_url": "", "insider_interview": None, "url": "", "alternate_url": {self.url}, "relations": \
[], "employer": {{"id": "", "name": "", "url": "", "alternate_url": "", "logo_urls": None, "vacancies_url": \
"", "accredited_it_employer": False, "trusted": False}}, "snippet": {{"requirement": "{self.requirement}", \
"responsibility": ""}}, "contacts": None, "schedule": {{"id": "", "name": ""}}, "working_days": [], \
"working_time_intervals": [], "working_time_modes": [], "accept_temporary": False, "professional_roles": \
[{{"id": "", "name": ""}}], "accept_incomplete_resumes": True, "experience": {{"id": "", "name": ""}}, \
"employment": {{"id": "", "name": ""}}, "adv_response_url": None, "is_adv_vacancy": False, "adv_context": None}}')

    @classmethod
    def __valid_salary(cls, salary):
        """Приватный метод проверки зарплаты"""
        if not salary:
            return 0
        else:
            return salary

    @classmethod
    def __verify_data(cls, some) -> int:
        """Валидация при сравнении вакансий"""
        if not isinstance(some, Vacancy):
            raise TypeError("Операнд справа должен иметь тип Vacancy")

        if some.salary != 0:
            return int(re.split('[- ]', some.salary)[0])
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


# if __name__ == "__main__":
#     vacancy1 = Vacancy("Геофизик", "<https://hh.ru/vacancy/123456>", None,
#                        "Требования: опыт работы от 1 года...")
#     print(f"For {vacancy1.name} salary {vacancy1.salary}")
#     print(vacancy1)
#     vacancy2 = Vacancy("Геолог", "<https://hh.ru/vacancy/123457>", "100000-150000 руб",
#                        "Требования: без опыта...")
#     print(f"For {vacancy2.name} salary {vacancy2.salary}")
#     print(vacancy2)
#     vacancy3 = Vacancy("Ведущий геолог", "<https://hh.ru/vacancy/123458>", "150000 руб",
#                        "Требования: опыта 3 года...")
#     print(f"For {vacancy3.name} salary {vacancy3.salary}")
#     print(vacancy3)
#
#     print(vacancy1 <= vacancy2)
