import pytest

from src.saver import JSONSaver
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy(
        "Тестировщик комфорта квартир",
        "350000-450000",
        "https://hh.ru/vacancy/93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    )


@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy(
        "Менеджер чатов, удалённо (в Яндекс)",
        "30000-44000",
        "https://hh.ru/vacancy/92223673",
        "Способен работать в команде. Способен принимать решения самостоятельно. Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
    )


@pytest.fixture
def vacancy_3() -> Vacancy:
    return Vacancy(
        "Менеджер по работе с клиентами (МЕРКАТОР)",
        "100000",
        "https://hh.ru/vacancy/93161709",
        "Опыт в продажах или с клиентами. Грамотная речь. Активность. Коммуникабельность.",
    )


@pytest.fixture
def vacancy_4() -> Vacancy:
    return Vacancy(
        "Менеджер по работе с клиентами (МЕРКАТОР)-2",
        "350000-450000",
        "https://hh.ru/vacancy/9316",
        "Опыт в продажах или с клиентами. Грамотная речь. Активность.",
    )


@pytest.fixture
def vacancies_test() -> list:
    return [
        {
            "name": "QA engineer",
            "salary": 0,
            "alternate_url": "https://hh.ru/vacancy/110110217",
            "requirement": "...части совершенствования процессов тестирования. Желание развиваться в автоматизации тест кейсов (Java или <highlighttext>Python</highlighttext>). Самостоятельность. Опыт автоматизации тест кейсов (Java, <highlighttext>Python</highlighttext>).",
        },
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
        },
    ]


@pytest.fixture
def vacancy_1_in_file() -> dict:
    return {
        "name": "Тестировщик комфорта квартир",
        "salary": {
            "from": 350000,
            "to": 450000,
            "currency": "RUR",
        },
        "alternate_url": "https://hh.ru/vacancy/93353083",
        "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным мышлением...",
    }


@pytest.fixture
def json_saver_test(tmp_path):
    directory = tmp_path / "sub"
    directory.mkdir()
    path_to_file = directory / "vacancy.json"
    return [JSONSaver(path_to_file), path_to_file]


@pytest.fixture
def vacancies_test_2() -> list:
    return [
        {
            "name": "QA engineer",
            "salary": 0,
            "alternate_url": "https://hh.ru/vacancy/110110217",
            "requirement": "...части совершенствования процессов тестирования. Желание развиваться в автоматизации тест кейсов (Java или <highlighttext>Python</highlighttext>). Самостоятельность. Опыт автоматизации тест кейсов (Java, <highlighttext>Python</highlighttext>).",
        }
    ]


@pytest.fixture
def vacancy_5() -> Vacancy:
    return Vacancy(
        "Python/Django Junior Backend-разработчик",
        "60000-90000",
        "https://hh.ru/vacancy/110134917",
        "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
    )


@pytest.fixture
def vacancies_test_4() -> list:
    return [
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
        },
        {
            "name": "Директор по информационным технологиям (CIO)",
            "salary": {
                "from": 1000000,
                "to": 0,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/109787570",
            "requirement": "Arch based linux - будет большим плюсом. Bash scripts (скрипты) - профи. <highlighttext>Python</highlighttext> базовые знания - будет большим плюсом. Ansible - будет большим плюсом. ",
        },
    ]


@pytest.fixture
def vacancies_test_3() -> list:
    return [
        {
            "name": "Директор по информационным технологиям (CIO)",
            "salary": {
                "from": 1000000,
                "to": 0,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/109787570",
            "requirement": "Arch based linux - будет большим плюсом. Bash scripts (скрипты) - профи. <highlighttext>Python</highlighttext> базовые знания - будет большим плюсом. Ansible - будет большим плюсом. ",
        },
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, docker, supervisor.",
        },
    ]

@pytest.fixture
def vacancies_from_hh_str():
    return """[{
      "id": "93161709",
      "premium": false,
      "name": "Менеджер по работе с клиентами (МЕРКАТОР)",
      "department": null,
      "has_test": false,
      "response_letter_required": false,
      "area": {
        "id": "88",
        "name": "Казань",
        "url": "https://api.hh.ru/areas/88"
      },
      "salary": {
        "from": 100000,
        "to": null,
        "currency": "RUR",
        "gross": true
      },
      "type": {
        "id": "open",
        "name": "Открытая"
      },
      "address": {
        "city": "Казань",
        "street": "Приволжский район, жилой массив Отары, Дорожная улица",
        "building": "1к10",
        "lat": 55.724135,
        "lng": 49.098078,
        "description": null,
        "raw": "Казань, Приволжский район, жилой массив Отары, Дорожная улица, 1к10",
        "metro": null,
        "metro_stations": [],
        "id": "15161689"
      },
      "response_url": null,
      "sort_point_distance": null,
      "published_at": "2024-02-13T17:06:04+0300",
      "created_at": "2024-02-13T17:06:04+0300",
      "archived": false,
      "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93161709",
      "show_logo_in_search": null,
      "insider_interview": null,
      "url": "https://api.hh.ru/vacancies/93161709?host=hh.ru",
      "alternate_url": "https://hh.ru/vacancy/93161709",
      "relations": [],
      "employer": {
        "id": "1060821",
        "name": "Рост Развитие Решение",
        "url": "https://api.hh.ru/employers/1060821",
        "alternate_url": "https://hh.ru/employer/1060821",
        "logo_urls": {
          "90": "https://hhcdn.ru/employer-logo/874868.jpeg",
          "240": "https://hhcdn.ru/employer-logo/874869.jpeg",
          "original": "https://hhcdn.ru/employer-logo-original/85446.jpg"
        },
        "vacancies_url": "https://api.hh.ru/vacancies?employer_id=1060821",
        "accredited_it_employer": false,
        "trusted": true
      },
      "snippet": {
        "requirement": "Опыт в продажах или с клиентами. Грамотная речь. Активность. Коммуникабельность.",
        "responsibility": "Работа с клиентами. Контроль остатков инструмента на складе. Работа с дебиторской задолженностью. Отчетность в установленной форме (1С, Битрикс 24)."
      },
      "contacts": null,
      "schedule": {
        "id": "fullDay",
        "name": "Полный день"
      },
      "working_days": [],
      "working_time_intervals": [],
      "working_time_modes": [],
      "accept_temporary": false,
      "professional_roles": [
        {
          "id": "70",
          "name": "Менеджер по продажам, менеджер по работе с клиентами"
        }
      ],
      "accept_incomplete_resumes": false,
      "experience": {
        "id": "between1And3",
        "name": "От 1 года до 3 лет"
      },
      "employment": {
        "id": "full",
        "name": "Полная занятость"
      },
      "adv_response_url": null,
      "is_adv_vacancy": false,
      "adv_context": null
    }]"""
