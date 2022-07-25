from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By  # Позволяет получить элементы по локаторам
from selenium.webdriver.support import expected_conditions as ec  # Ожидание страницы
from selenium.webdriver.support.ui import WebDriverWait  # Ожидание страницы
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 5, 1)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'parial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME}
        return locating[find_by]

    def is_visible(self, find_by: str, locator: str,
                   locator_name: str = None) -> WebElement:  # Ожидание видимости элемента на экране.
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:  # присутствие элемента
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str,
                       locator_name: str = None) -> WebElement:  # ожидание невидимости элемента
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[
        WebElement]:  # Ожидание видимости нескольктх элементов
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[
        WebElement]:  # Ожидание присутствия элементв
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:  # текст элементов
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str,
                            i: int = 0) -> WebElement:  # найти элемент по тексту
        return [element for element in elements if element.text == name][i]


