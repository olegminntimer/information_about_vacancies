import requests

from abc import ABC, abstractmethod
from pathlib import Path


class Parser(ABC):
    """Абстрактный класс подключения к API и получения вакансий."""
    @abstractmethod
    def __connection_to_api(self):
        """Абстрактный метод подключения к API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        """Абстрактный метод получения коллекции вакансий"""
        pass


class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    """
    def __init__(self): #, file_worker):
        """Конструктор класса HeadHunter"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        self._Parser__connection_to_api()
        super().__init__()#file_worker)

    def _Parser__connection_to_api(self):
        """Приватный метод подключения к API"""
        return requests.get(self.__url, headers=self.__headers, params=self.__params)

    def get_vacancies(self, keyword: str="") -> None:
        """Метод загрузки вакансий с НН"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self._Parser__connection_to_api()
            if response.status_code != 200:
                continue
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.__params['page'] += 1

# if __name__ == "__main__":
#     BASE_DIR = Path(__file__).resolve().parent.parent
#     hh_api = HeadHunterAPI()
#     hh_api.get_vacancies('python')
#     for i in range(10):
#         print(hh_api.vacancies[i])
