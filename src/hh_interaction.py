from abc import ABC, abstractmethod

import requests

from src.utils import list_formatter


class Parser(ABC):
    """Абстрактный класс подключения к API и получения вакансий."""

    @abstractmethod
    def get_vacancies(self, keyword: str):
        """Абстрактный метод получения коллекции вакансий."""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter."""

    def __init__(self):
        """Конструктор класса HeadHunter"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        super().__init__()

    def get_vacancies(self, keyword: str = "") -> list:
        """Метод загрузки вакансий с НН"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            # if response.status_code != 200:
            #     continue
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1
        return self.vacancies


# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     vacancies_list = hh_api.get_vacancies('python')
#     print(vacancies_list)
