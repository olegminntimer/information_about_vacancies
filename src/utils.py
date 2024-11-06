import json
import re
from typing import Any


def range_bounds_check(range_numbers: Any) -> list:
    """Функция возвращает список [левая граница, правая граница] из введенной строки диапазона."""
    if isinstance(range_numbers, str):
        pattern = re.compile(r'\d+')
        left_bound = pattern.match(range_numbers)
        if left_bound:
            right_bound = pattern.search(range_numbers, pos=len(left_bound.group(0)))
            if right_bound:
                return [int(left_bound.group(0)), int(right_bound.group(0))]
            else:
                return [int(left_bound.group(0)), 0]
        else:
            right_bound = pattern.search(range_numbers)
            if right_bound:
                return [0, int(right_bound.group(0))]
            else:
                return []
    elif isinstance(range_numbers, int):
        if range_numbers > 0:
            return [range_numbers, 0]
        else:
            return []


def filter_vacancies(vacancies: list, filter_words: list) -> list:
    """Функция ищет вакансии по ключевым словам."""
    filtered_vacancies_ = []
    pattern = "(?:" + "|".join(filter_words) + ")"
    for vacancy in vacancies:
        if vacancy["requirement"]:
            if bool(re.search(pattern, vacancy["requirement"], flags=re.IGNORECASE)):
                filtered_vacancies_.append(vacancy)
    return filtered_vacancies_


def get_vacancies_by_salary(vacancies:list, salary_range: str) -> list:
    """Функция делает выборку по диапазону предлагаемой зарплаты"""
    limits = range_bounds_check(salary_range)
    if not limits:
        print("Не введен диапазон зарплаты!")
        return []
    ranged_vacancies_ = []
    for vacancy in vacancies:
        if vacancy["salary"]:
            if limits[0] <= vacancy["salary"]["from"] <= limits[1]:
                ranged_vacancies_.append(vacancy)
                continue
            if limits[0] <= vacancy["salary"]["to"] <= limits[1]:
                ranged_vacancies_.append(vacancy)
    return ranged_vacancies_


def sort_vacancies(vacancies:list) -> list:
    """Функция сортирует список вакансий по убыванию предлагаемой зарплаты."""
    return sorted(vacancies, key=lambda x: (x["salary"]["from"], x["salary"]["to"]), reverse=True)


def get_top_vacancies(vacancies: list, top_n: int):
    """Функция возвращает первые top_n вакансии по зарплате"""
    return vacancies[:top_n]


def print_vacancies(vacancies: list) -> None:
    """Функция выводит на экран вакансии из выбранного списка"""
    for i in vacancies:
        print(json.dumps(i, ensure_ascii=False, indent=4))
