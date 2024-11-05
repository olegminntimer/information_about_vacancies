
def optimized_list(vacancies_from_hh) -> list:
    """Метод выборки полей вакансий: название, ссылка, зарплата, валюта, требования"""
    optim = []
    for row in vacancies_from_hh:
        if row["salary"]:
            salary = f"{row["salary"]["from"]}-{row["salary"]["to"]} {row["salary"]["currency"]}"
        else:
            salary = None
        optim.append({"name" :row["name"], "url": row["alternate_url"], "salary" : salary, "requirement": row["snippet"]["requirement"]})
    return optim


def filter_vacancies(vacancies_list, filter_words):
    pass


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    pass


def sort_vacancies(ranged_vacancies):
    pass


def get_top_vacancies(sorted_vacancies, top_n):
    pass


def print_vacancies(top_vacancies):
    pass
