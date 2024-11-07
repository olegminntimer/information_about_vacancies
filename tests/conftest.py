import pytest

from src.saver import JSONSaver
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_1() -> Vacancy:
    return Vacancy(
        "Тестировщик комфорта квартир",
        "350000-450000",
        "https://hh.ru/vacancy/93353083",
        "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. \
        Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным \
        мышлением...",
    )


@pytest.fixture
def vacancy_2() -> Vacancy:
    return Vacancy(
        "Менеджер чатов, удалённо (в Яндекс)",
        "30000-44000",
        "https://hh.ru/vacancy/92223673",
        "Способен работать в команде. Способен принимать решения самостоятельно. \
        Готов учиться и узнавать новое. Опыт работы в колл-центре или службе...",
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
            "requirement": "...части совершенствования процессов тестирования. Желание развиваться в \
            автоматизации тест кейсов (Java или <highlighttext>Python</highlighttext>). \
            Самостоятельность. Опыт автоматизации тест кейсов (Java, <highlighttext>Python</highlighttext>).",
        },
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
        "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь. \
        Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. Обладать системным \
        мышлением...",
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
            "requirement": "...части совершенствования процессов тестирования. Желание развиваться в \
            автоматизации тест кейсов (Java или <highlighttext>Python</highlighttext>). \
            Самостоятельность. Опыт автоматизации тест кейсов (Java, <highlighttext>Python</highlighttext>).",
        }
    ]


@pytest.fixture
def vacancy_5() -> Vacancy:
    return Vacancy(
        "Python/Django Junior Backend-разработчик",
        "60000-90000",
        "https://hh.ru/vacancy/110134917",
        "Наличие примеров работ в git. Опыт работы с асинхронным \
        <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, \
        docker, supervisor.",
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
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным \
            <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, \
            docker, supervisor.",
        },
        {
            "name": "Директор по информационным технологиям (CIO)",
            "salary": {
                "from": 1000000,
                "to": 0,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/109787570",
            "requirement": "Arch based linux - будет большим плюсом. Bash scripts (скрипты) - профи. \
            <highlighttext>Python</highlighttext> базовые знания - будет большим плюсом. Ansible - \
            будет большим плюсом. ",
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
            "requirement": "Arch based linux - будет большим плюсом. Bash scripts (скрипты) - профи. \
            <highlighttext>Python</highlighttext> базовые знания - будет большим плюсом. Ansible - \
            будет большим плюсом. ",
        },
        {
            "name": "Python/Django Junior Backend-разработчик",
            "salary": {
                "from": 60000,
                "to": 90000,
                "currency": "RUR",
            },
            "alternate_url": "https://hh.ru/vacancy/110134917",
            "requirement": "Наличие примеров работ в git. Опыт работы с асинхронным \
            <highlighttext>python</highlighttext>. Опыт деплоя проектов. Опыт работы с celery, redis, \
            docker, supervisor.",
        },
    ]
