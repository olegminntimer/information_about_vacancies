import requests

from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс подключения к API и получения вакансий."""
    @abstractmethod
    def __connection_to_api(self):
        """Абстрактный метод подключения к API."""
        pass

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
        self._Parser__connection_to_api()
        super().__init__()

    def _Parser__connection_to_api(self):
        """Приватный метод подключения к API"""
        return requests.get(self.__url, headers=self.__headers, params=self.__params)

    def get_vacancies(self, keyword: str="") -> list:
        """Метод загрузки вакансий с НН"""
        self.__params['text'] = keyword
        print("Поиск вакансий ", end="")
        while self.__params.get('page') != 20:
            response = self._Parser__connection_to_api()
            if response.status_code != 200:
                continue
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1
            print("#", end="")
        return self.vacancies

    def optimized_list(self) -> list:
        """Метод выборки полей вакансий: название, ссылка, зарплата, валюта, требования"""
        optim = []
        for row in self.vacancies:
            if row["salary"]:
                salary = f"{row["salary"]["from"]}-{row["salary"]["to"]} {row["salary"]["currency"]}"
            else:
                salary = None
            optim.append({"name":row["name"], "url": row["alternate_url"], "salary" : salary, "requirement": row["snippet"]["requirement"]})
        return optim

# if __name__ == "__main__":
#     hh_api = HeadHunterAPI()
#     vacancies_list = hh_api.get_vacancies('python')
#     vacancies_optimized = hh_api.optimized_list()
#
#     for i in range(10):
#         print(vacancies_optimized[i])
