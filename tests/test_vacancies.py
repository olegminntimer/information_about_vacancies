import pytest

from src.vacancies import Vacancy


def test_vacancy_init(vacancy_1: Vacancy) -> None:
    """Проверяем метод конвертации вакансии в словарь для добавления в файл."""
    assert vacancy_1.name == "Тестировщик комфорта квартир"
    assert vacancy_1.salary == {"currency": "RUR", "from": 350000, "to": 450000}
    assert vacancy_1.url == "https://hh.ru/vacancy/93353083"
    assert (
        vacancy_1.requirement
        == "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать \
        навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением..."
    )


def test_vacancy_eq(vacancy_1: Vacancy, vacancy_4: Vacancy) -> None:
    """Проверяем равенство по зарплате "from" между вакансиями."""
    assert vacancy_1 == vacancy_4


def test_vacancy_lt(vacancy_1: Vacancy, vacancy_2: Vacancy) -> None:
    """Проверяем "меньше" по зарплате "from" между вакансиями."""
    assert vacancy_2 < vacancy_1


# def test_vacancy_lt_error(vacancy_1: Vacancy):
#     with pytest.raises(TypeError):
#         vacancy_1 > "vacancy_2"


def test_vacancy_le(vacancy_1: Vacancy, vacancy_2: Vacancy, vacancy_4: Vacancy) -> None:
    """Проверяем "меньше или равно" по зарплате "from" между вакансиями."""
    assert vacancy_4 <= vacancy_1
    assert vacancy_2 <= vacancy_1


def test_vacancy_to_file(vacancy_1: Vacancy) -> None:
    """Проверяем форматирование вакансии для записи в файл."""
    assert vacancy_1.to_file() == {
        "name": "Тестировщик комфорта квартир",
        "salary": {"currency": "RUR", "from": 350000, "to": 450000},
        "alternate_url": "https://hh.ru/vacancy/93353083",
        "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. \
        Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать \
        системным мышлением...",
    }
