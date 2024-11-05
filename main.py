import json

from src.hh_interaction import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():
    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    # salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    # Ищем вакансии по запросу
    # hh_api = HeadHunterAPI()
    # vacancies_list = hh_api.get_vacancies(search_query)
    with open('./data/vacancies_hh.json', encoding="utf-8") as file:
        vacancies_list = json.load(file)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    print(filtered_vacancies)

    # ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    #
    # sorted_vacancies = sort_vacancies(ranged_vacancies)
    #
    # top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #
    # print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
