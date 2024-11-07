import unittest
from unittest.mock import MagicMock, patch

from src.hh_interaction import HeadHunterAPI


class TestHeadHunterAPI(unittest.TestCase):

    @patch("requests.get")  # Мокаем requests.get
    def test_get_vacancies(self, mock_get):
        # Создаем замоканный ответ, который будет возвращаться вместо реального запроса
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "items": [{"name": "Python Developer", "salary": "1000"}, {"name": "Data Scientist", "salary": "1500"}]
        }
        mock_get.return_value = mock_response
        # Создаем экземпляр класса HeadHunterAPI
        hh = HeadHunterAPI()
        # Вызываем метод get_vacancies
        hh.get_vacancies("Python Developer")
        # Проверяем, что вакансии были добавлены
        self.assertGreater(len(hh.vacancies), 0)
        self.assertEqual(hh.vacancies[0]["name"], "Python Developer")
        # Проверяем, что requests.get вызывался с правильными аргументами
        mock_get.assert_called_with(
            "https://api.hh.ru/vacancies",
            headers={"User-Agent": "HH-User-Agent"},
            params={"text": "Python Developer", "page": 0, "per_page": 100},
        )


# if __name__ == '__main__':
#     unittest.main()
