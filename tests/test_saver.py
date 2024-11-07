import json
from email.generator import Generator

from src.saver import JSONSaver
from src.vacancies import Vacancy


def test_saver_save_to(vacancies_test: list, json_saver_test: list) -> None:
    """Тестирование сохранения списка вакансий в файл."""
    json_saver_test[0].save_to(vacancies_test)
    with open(json_saver_test[1], encoding="utf-8") as file:
        vacancies_from_file = json.load(file)
    assert len(vacancies_from_file) == 2
    assert vacancies_from_file[0] == {
        "name": "QA engineer",
        "salary": 0,
        "alternate_url": "https://hh.ru/vacancy/110110217",
        "requirement": "...части совершенствования процессов тестирования. Желание развиваться в \
        автоматизации тест кейсов (Java или <highlighttext>Python</highlighttext>). Самостоятельность. \
        Опыт автоматизации тест кейсов (Java, <highlighttext>Python</highlighttext>).",
    }


def test_saver_add_vacancy(vacancy_1: Vacancy, vacancy_1_in_file: dict, json_saver_test: list, vacancies_test: list) -> None:
    """Тестирование добавления вакансии в список вакансий из файла."""
    json_saver_test[0].save_to(vacancies_test)
    json_saver_test[0].add_vacancy(vacancy_1)
    with open(json_saver_test[1], encoding="utf-8") as file:
        vacancies_from_file = json.load(file)
    assert vacancies_from_file[2] == vacancy_1_in_file


def test_saver_delete_vacancy(vacancy_5: Vacancy, json_saver_test: list, vacancies_test: list, vacancies_test_2: list) -> None:
    """Тестирование удаления вакансии из списка вакансий из файла."""
    json_saver_test[0].save_to(vacancies_test)
    json_saver_test[0].delete_vacancy(vacancy_5)
    with open(json_saver_test[1], encoding="utf-8") as file:
        vacancies_from_file = json.load(file)
    assert vacancies_from_file == vacancies_test_2


def test_saver_add_vacancy_incorrect_format(capsys, json_saver_test: list, vacancies_test: list) -> None:
    """Тестирование добавления вакансии в некорректном формате в список вакансий из файла."""
    json_saver_test[0].save_to(vacancies_test)
    json_saver_test[0].add_vacancy("vacancy_1")
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Неправильный формат вакансии!"


def test_saver_delete_vacancy_incorrect_format(capsys, json_saver_test: list, vacancies_test: list) -> None:
    """Тестирование удаления вакансии в некорректном формате из списка вакансий из файла."""
    json_saver_test[0].save_to(vacancies_test)
    json_saver_test[0].delete_vacancy("vacancy_5")
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Неправильный формат вакансии!"


def test_saver_delete_vacancy_empty(capsys, vacancy_1: Vacancy, json_saver_test: list, vacancies_test: list) -> None:
    """Тестирование удаления отсутствующей вакансии из списка вакансий из файла."""
    json_saver_test[0].save_to(vacancies_test)
    json_saver_test[0].delete_vacancy(vacancy_1)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Такой вакансии нет в файле."
