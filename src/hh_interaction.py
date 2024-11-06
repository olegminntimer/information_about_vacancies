import requests

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс подключения к API и получения вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword):
        """Абстрактный метод получения коллекции вакансий."""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Конструктор класса HeadHunter"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()


    def get_vacancies(self, keyword: str = "") -> list:
        """Метод загрузки вакансий с НН"""
        self.__params['text'] = keyword
        print("Поиск вакансий ", end="")
        while self.__params.get('page') != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                continue
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1
            print("#", end="")
        print()
        vacancies_formatted = []
        for vacancy in self.vacancies:
            if vacancy["salary"]:
                if not(vacancy["salary"]["from"]):
                    vacancy["salary"]["from"] = 0
                if not(vacancy["salary"]["to"]):
                    vacancy["salary"]["to"] = 0
            else:
                vacancy["salary"] = 0
            vacancies_formatted.append(
                {"name": vacancy["name"], "salary": vacancy["salary"], "alternate_url": vacancy["alternate_url"],
                 "requirement": vacancy["snippet"]["requirement"]})
        return vacancies_formatted


# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     vacancies_list = hh_api.get_vacancies('python')
#     print(vacancies_list)
