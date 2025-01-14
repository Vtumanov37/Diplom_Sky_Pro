from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_button = (By.CSS_SELECTOR, "input[value='поиск']")

    def search_by_year(self, year):
        self._enter_text(By.ID, "year", str(year))
        self._click_search_button()

    def search_by_title(self, title):
        self._enter_text(By.ID, "find_film", title)
        self._click_search_button()

    def search_title_negativ(self, title):
        self._enter_text(By.ID, "find_film", title)
        self._click_search_button()

    def search_by_genre(self, genre_value):
        genre_option = self.driver.find_element(
            By.XPATH, f"//input[@value='{genre_value}'] | //option[text()='история']")
        genre_option.click()
        self._click_search_button()

    def search_by_actor(self, title, actor):
        self._enter_text(By.ID, "find_film", title)
        self._enter_text(By.NAME, "m_act[actor]", actor)
        self._click_search_button()

    def _enter_text(self, by, identifier, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((by, identifier)))
        element.clear()
        element.send_keys(text)

    def _select_dropdown_option(self, by, dropdown_id, option_xpath):
        dropdown = self.driver.find_element(by, dropdown_id)
        dropdown.click()
        option = self.driver.find_element(By.XPATH, option_xpath)
        option.click()

    def _click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def wait_for_element(self, by, value, timeout=8):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def wait_for_element_with_text(self, by, value, text, timeout=15):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.text_to_be_present_in_element((by, value), text)
            )
        except TimeoutException:
            print(f"Element with locator {by} and value {value} containing text '{
                  text}' not found after {timeout} seconds.")
            return False
