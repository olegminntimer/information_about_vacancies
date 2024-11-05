import json
import os.path
from abc import ABC, abstractmethod
from pathlib import Path

from src.hh_interaction import HeadHunterAPI
from src.vacancies import Vacancy


class Saver(ABC):
    """Абстрактный класс для сохранения в файл информации о вакансиях."""

    @abstractmethod
    def save_to(self, vacancies_list: list):
        """Абстрактный метод сохранения информации в файл."""
        pass

    @abstractmethod
    def add_vacancy(self, vacancy: str):
        """Абстрактный метод добавления информации о вакансии в файл."""
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: str):
        """Абстрактный метод удаления информации о вакансии из файла."""
        pass


class JSONSaver(Saver):
    """Класс для сохранения информации в JSON-файл."""
    BASE_DIR = Path(__file__).resolve().parent.parent

    def __init__(self, filename: str = str(BASE_DIR / "data" / "vacancies_hh.json")):
        """Конструктор класса JSONSaver."""
        self.__filename = filename

    def save_to(self, vacancies_list: list) -> None:
        """Метод сохранения информации в файл."""
        new_vacancies_file = vacancies_list
        if os.path.isfile(self.__filename):
            # считываем из файла сохраненный ранее список
            with open(self.__filename, encoding="utf-8") as file:
                vacancies_file = json.load(file)
            # Добавляем к списку в файле список с новым запросом
            vacancies_file.extend(vacancies_list)
            # убираем дубликаты
            new_vacancies_file = []
            for dictionary in vacancies_file:
                if dictionary not in new_vacancies_file:
                    new_vacancies_file.append(dictionary)
        # записываем в файл измененный файл
        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(new_vacancies_file, file, ensure_ascii=False)

    def add_vacancy(self, vacancy: [Vacancy | dict]) -> None:
        """Метод добавления информации о вакансии в файл."""
        # считываем из файла сохраненный ранее список
        with open(self.__filename, encoding="utf-8") as file:
            vacancies = json.load(file)
        if isinstance(vacancy, Vacancy):
            # vacancy = {"name": vacancy.name, "url": vacancy.url, "salary": vacancy.salary,
            #            "requirement": vacancy.requirement}
            # "salary": {"from": 1000000, "to": null, "currency": "RUR", "gross": false}

        # Проверяем вакансию на совпадение по адресу "alternate_url"
        is_presence = False
        for i in vacancies:
            if vacancy["alternate_url"] == i["alternate_url"]:
                is_presence = True
        # Если нет совпадений, то добавляем в файл
        if not is_presence:
            vacancies.append(vacancy)
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(vacancies, file, ensure_ascii=False)

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления информации о вакансии из файла."""
        with open(self.__filename, encoding="utf-8") as file:
            vacancies = json.load(file)
        vacancy = {"name": vacancy.name, "url": vacancy.url, "salary": vacancy.salary,
                   "requirement": vacancy.requirement}
        is_presence = False
        for i in vacancies:
            if vacancy["url"] == i["url"]:
                is_presence = True
                vacancies.remove(i)
        if is_presence:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(vacancies, file, ensure_ascii=False)
        else:
            print("Такой вакансии нет в файле.")


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    vacancies_list = hh_api.get_vacancies('python')
    #     vacancies_optimized = hh_api.optimized_list()
    json_saver = JSONSaver()
    json_saver.save_to(vacancies_list)
#     vacancy1 = Vacancy("Геофизик", "<https://hh.ru/vacancy/123456>", None,
#                        "Требования: опыт работы от 1 года...")
#     json_saver.add_vacancy(vacancy1)
#     json_saver.delete_vacancy(vacancy1)
