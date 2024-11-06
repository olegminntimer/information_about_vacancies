import json
import re


def filter_vacancies(vacancies: list, filter_words: list) -> list:
    """Метод ищет вакансии по ключевым словам."""
    filtered_vacancies_ = []
    pattern = "(?:" + "|".join(filter_words) + ")"
    for vacancy in vacancies:
        if vacancy["snippet"]["requirement"]:
            if bool(re.search(pattern, vacancy["snippet"]["requirement"], flags=re.IGNORECASE)):
                filtered_vacancies_.append(vacancy)
    return filtered_vacancies_


def get_vacancies_by_salary(vacancies:list, salary_range: str) -> list:
    """Метод делает выборку по диапазону предлагаемой зарплаты"""
    salary_limit = []
    for i in re.split('[- ]', salary_range):
        if i != '':
            salary_limit.append(i)
    try:
        left_limit = int(salary_limit[0])
    except TypeError:
        left_limit = 0
    try:
        right_limit = int(salary_limit[1])
    except TypeError:
        right_limit = 0

    ranged_vacancies_ = []
    print(salary_limit)
    if (left_limit > 0) and (right_limit > 0):
        for vacancy in vacancies:
            if vacancy["salary"]:
                if vacancy["salary"]["from"]:
                    if salary_limit[0] <= vacancy["salary"]["from"] <= salary_limit[1]:
                        ranged_vacancies_.append(vacancy)
                    else:
                        if salary_limit[0] <= vacancy["salary"]["to"] <= salary_limit[1]:
                            ranged_vacancies.append(vacancy)
    elif isinstance(salary_limit[0], int) and not(isinstance(salary_limit[1], int)):
        for vacancy in vacancies:
            if vacancy["salary"]:
                if vacancy["salary"]["from"]:
                    if salary_limit[0] <= vacancy["salary"]["from"]:
                        ranged_vacancies_.append(vacancy)
    else:
        print("Не верно задан диапазон зарплат!")
        return []
    return ranged_vacancies

    print(ranged_vacancies)




def sort_vacancies(ranged_vacancies):
    pass


def get_top_vacancies(sorted_vacancies, top_n):
    pass


def print_vacancies(top_vacancies):
    pass

if __name__ == "__main__":
    with open('../data/vacancies_hh.json', encoding="utf-8") as file:
        vacancies_list = json.load(file)
    #
    # filtered_vacancies = filter_vacancies(vacancies_list, ['java', 'git'])
    # print(filtered_vacancies)
    ranged_vacancies = get_vacancies_by_salary(vacancies_list,"50000 - 200000 rub")
    print(ranged_vacancies)
