import json
import re


def filter_vacancies(vacancies_list_: list, filter_words: list) -> list:
    """Функция ищет вакансии по ключевым словам."""
    filtered_vacancies_ = []
    pattern = "(?:" + "|".join(filter_words) + ")"
    for vacancy in vacancies_list_:
        if vacancy["snippet"]["requirement"]:
            if bool(re.search(pattern, vacancy["snippet"]["requirement"], flags=re.IGNORECASE)):
                filtered_vacancies_.append(vacancy)
    return filtered_vacancies_


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    pass


def sort_vacancies(ranged_vacancies):
    pass


def get_top_vacancies(sorted_vacancies, top_n):
    pass


def print_vacancies(top_vacancies):
    pass

if __name__ == "__main__":
    with open('../data/vacancies_hh.json', encoding="utf-8") as file:
        vacancies_list = json.load(file)

    filtered_vacancies = filter_vacancies(vacancies_list, ['java', 'git'])
    print(filtered_vacancies)