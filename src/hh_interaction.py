import requests
import pandas as pd

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс подключения к API и получения вакансий."""

    # @abstractmethod
    # def __connection_to_api(self):
    #     """Приватный абстрактный метод подключения к API."""
    #     pass

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
        self.__params = {'text': '', 'page': 0, 'per_page': 10}
        self.vacancies = []
        # self._Parser__connection_to_api()
        super().__init__()

    # def _Parser__connection_to_api(self):
    #     """Приватный метод подключения к API"""
    #     return requests.get(self.__url, headers=self.__headers, params=self.__params)

    def get_vacancies(self, keyword: str = "") -> list:
        """Метод загрузки вакансий с НН"""
        self.__params['text'] = keyword
        print("Поиск вакансий ", end="")
        while self.__params.get('page') != 2:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code != 200:
                continue
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1
            print("#", end="")
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
