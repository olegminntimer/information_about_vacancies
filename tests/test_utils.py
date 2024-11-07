from src.utils import filter_vacancies, get_top_vacancies, get_vacancies_by_salary, range_bounds_check, sort_vacancies


def test_range_bounds_check() -> None:
    assert range_bounds_check("100 200") == [100, 200]
    assert range_bounds_check("aaa123mkgbg") == [0, 123]
    assert range_bounds_check("923mkgbg") == [923, 0]
    assert range_bounds_check("asddfamkgbg") == []
    assert range_bounds_check("375 - 345 RUR") == [375, 345]
    assert range_bounds_check(150000) == [150000, 0]
    assert range_bounds_check("!@#$%^&*~") == []


def test_filter_vacancies(vacancies_test: list) -> None:
    filtered_vacancies = filter_vacancies(vacancies_test, ["redis"])
    assert filtered_vacancies == [
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным \
            <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, \
            redis, docker, supervisor.",
        }
    ]


def test_get_vacancies_by_salary(vacancies_test: list) -> None:
    ranged_vacancies = get_vacancies_by_salary(vacancies_test, "50000-100000")
    assert ranged_vacancies == [
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным \
            <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, \
            redis, docker, supervisor.",
        }
    ]


def test_sort_vacancies(vacancies_test_4: list, vacancies_test_3: list) -> None:
    sorted_vacancies = sort_vacancies(vacancies_test_4)
    assert sorted_vacancies == vacancies_test_3


def test_get_top_vacancies_2(vacancies_test_3: list) -> None:
    top_vacancies = get_top_vacancies(vacancies_test_3, 2)
    assert top_vacancies == vacancies_test_3


def test_get_top_vacancies_1(vacancies_test_3: list) -> None:
    top_vacancies = get_top_vacancies(vacancies_test_3, 1)
    assert top_vacancies == [
        {
            "name": "Директор по информационным технологиям (CIO)",
            "salary": {
                "from": 1000000,
                "to": 0,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/109787570",
            "requirement": "Arch based linux - будет большим плюсом. Bash scripts (скрипты) - \
            профи. <highlighttext>Python</highlighttext> базовые знания - будет большим плюсом. \
            Ansible - будет большим плюсом. ",
        }
    ]
