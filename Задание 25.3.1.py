import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.set_window_size(1200, 700)
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('herip@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('88888888')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    pytest.driver.find_element_by_link_text('Мои питомцы').click()
    box = pytest.driver.find_element_by_xpath('//*[@class="task3 fill"]/div')

    petsNumber = int(box.text.split('\n')[1].split(':')[1].strip())

    table_div = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'all_my_pets'))
    )

    assert table_div is not None
    pytest.driver.implicitly_wait(2)

    petsRows = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr') #Количество питомцев

    assert len(petsRows) == petsNumber #Присутствуют все питомцы

    images_count = 0
    pets_name = []
    pets = []
    for i in range(len(petsRows)):
        image = petsRows[i].find_element_by_xpath("*/img")
        name = petsRows[i].find_element_by_xpath("td[1]")
        kind = petsRows[i].find_element_by_xpath("td[2]")
        age = petsRows[i].find_element_by_xpath("td[3]")

        assert name.text != '' # Берём i-го питомца и смотрим, что элемент, который должен содержать его имя, имеет не пустой текст.
        assert kind.text != ''  # Берём i-го питомца и смотрим, что элемент, который должен содержать его виды, имеет не пустой текст.
        assert age.text != '' # Берём i-го питомца и смотрим, что элемент, который должен содержать его возраста, имеет не пустой текст.

        if image.get_attribute('src') != '': # Каждая картинка имеет атрибут src. Мы просто проверяем, что путь, указанный в атрибуте src, не пустой.
            images_count += 1

        pets_name.append(name)
        pets.append(Pet(name.text, kind.text, age.text))

    # pets.append(Pet("a", "b", "1"))
    # pets.append(Pet("a", "b", "1"))
    # print(pets)

    assert images_count > petsNumber / 2 # проверяем, что фото есть хотя бы у половины питомцев
    assert len(pets_name) == len(set(pets_name)) # Проверяем что все имена разные

    assert len(pets) == len(set(pets)) # Проверяем что все питомцы разные


class Pet(object):
    name = ""
    kind = ""
    age = ""

    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.kind == other.kind and self.age == other.age

    def __hash__(self):
        return hash(('name', self.name, 'kind', self.kind, 'age', self.age))
