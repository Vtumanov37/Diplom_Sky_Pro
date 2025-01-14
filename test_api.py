import requests
import allure
from config import URL_API, HEADERS


@allure.title("Поиск фильма по названию")
@allure.description("Выполнение теста на поиск контента по названию")
@allure.id(1)
@allure.severity("Критический")
def test_search_content_by_title():

    with allure.step("Указываем GET запроса с ID"):
        response = requests.get(
            f"{URL_API}movie/search?page=1&limit=10&query=%D1%82%D0%B5%D1%80%D0%BC%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80", headers=HEADERS)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.title("Поиск актера, режиссера и т.д.")
@allure.description("Выполнение теста на поиск персоны")
@allure.id(2)
@allure.severity("Критический")
def test_search_person_by_name():

    with allure.step("Указываем GET запрос с названием контента"):
        response = requests.get(
            f"{URL_API}/person/search?page=1&limit=10&query=%D0%91%D0%B5%D0%B7%D1%80%D1%83%D0%BA%D0%BE%D0%B2", headers=HEADERS)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.title("Поиск фильмов с рейтингом 9-10")
@allure.description("Выполнение теста на поиск контента по параметру 'рейтинг'")
@allure.id(3)
@allure.severity("Критический")
def test_search_content_by_rating():

    with allure.step("Отправка GET запроса на"):
        response = requests.get(
            f"{URL_API}/movie?page=1&limit=10&rating.kp=9-10", headers=HEADERS)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.title("Поиск по типу(мультфильм) и году(2020)")
@allure.description("Выполнение теста на поиск по типу контента и году выхода")
@allure.id(4)
@allure.severity("Критический")
def test_search_content_type_and_year():

    with allure.step("Отправка GET запроса с ошибкой"):
        response = requests.get(
            f"{URL_API}/movie?page=1&limit=10&typeNumber=3&year=2020", headers=HEADERS)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200


@allure.title("Поиск фильма (Негативный)")
@allure.description("Выполнение теста на поиск фильма с несуществующим ID")
@allure.id(5)
@allure.severity("Критический")
def test_search_content_id_out_of_bounds():

    with allure.step("Отправляем GET запрос с несуществующим ID"):
        response = requests.get(f"{URL_API}/movie/0", headers=HEADERS)

    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 400
