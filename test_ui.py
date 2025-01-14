import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from search_page import SearchPage
from config import BASE_URL


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    driver.get(BASE_URL)
    return SearchPage(driver)


@allure.title("Поиск по фильтру год")
@allure.description("Выполняет тест на поиск контента по выбранному году.")
@allure.id(1)
@allure.severity("Критический")
def test_search_by_year(search_page):

    with allure.step("В методе указываем год"):
        search_page.search_by_year(2024)

    with allure.step("Метод проверяет, что контент соответствует году"):
        year_element = search_page.wait_for_element(By.CLASS_NAME, "year")
        assert year_element.text == "2024", f"Expected year to be 2024, but got {
            year_element.text}"


@allure.title("Поиск фильма")
@allure.description("Тест на поиск фильма по названию.")
@allure.id(2)
@allure.severity("Критический")
def test_search_by_title(search_page):

    with allure.step("В методе указываем название фильма"):
        search_page.search_by_title("Матрица")

    with allure.step("Метод проверяет, что контент соответствует искомому фильму."):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "The Matrix")
        assert is_content_found, "Expected to find content 'The Matrix'"


@allure.title("Поиск фильма (Негативный) ")
@allure.description("Тест на поиск несуществующего фильма по названию.")
@allure.id(3)
@allure.severity("Критический")
def test_search_title_negativ(search_page):

    with allure.step("В методе указываем название фильма"):
        search_page.search_by_title("Квадроберы в космосе")

    with allure.step("Метод проверяет, что контент соответствует искомому фильму."):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "textorangebig", "К сожалению, по вашему запросу ничего не найдено...")
        assert is_content_found, "К сожалению, по вашему запросу ничего не найдено..."


@allure.title("Поиск контента по жанру")
@allure.description("Выполнение теста на поиск контента по жанру")
@allure.id(4)
@allure.severity("Критический")
def test_search_by_genre(search_page):

    with allure.step("В методе указываем жанр контента"):
        search_page.search_by_genre("история")

    with allure.step("Метод проверяет, что найденный контент относится к искомому жанру"):
        is_genre_found = search_page.wait_for_element_with_text(
            By.XPATH, "//span[@class='gray' and contains(., 'история')]", "история")
        assert is_genre_found, "Expected to find content with genre 'история'"


@allure.title("Поиск фильма и персоны")
@allure.description("Выполнение теста на поиск контента по актеру")
@allure.id(5)
@allure.severity("Критический")
def test_search_by_actor(search_page):

    with allure.step("В методе указываем название фильма и персону"):
        search_page.search_by_actor("Константин", "Киану Ривз")

    with allure.step("Метод проверяет, что найденный контент соответствует указанному."):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "Constantine")
        assert is_content_found, "Expected to find content 'Constantine'"
