import pytest
from time import sleep
from pom import page_objects
from base import seleniumbase

# pytest -s -v
# @pytest.mark.usefixtures ("setup")

class TestHomePage:
    @pytest.mark.positive
    @pytest.mark.auth
    @pytest.fixture(autouse=True)
    def test_registration(self):  # Регистрация
        page_objects.SearchHelper(self.driver).click_on_the_registration_button()
        # sleep(5)
        page_objects.SearchHelper(self.driver).enter_word_EMAIL('herip@mail.ru')
        # sleep(2)
        page_objects.SearchHelper(self.driver).enter_word_PASS('38743988Xx')
        sleep(4)
        page_objects.SearchHelper(self.driver).click_on_the_registration_COME()
        sleep(5)
        assert page_objects.SearchHelper(
            self.driver).PAGE_opening_check().text == "Шишин Артем"  # Проверяем, что мы оказались на главной странице пользователя
        # assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"  # Проверяем, что мы оказались на главной странице пользователя

    @pytest.mark.positive
    def test_Search_favorites(self):  # Находим товар в поиске и добавляем в избранное
        page_objects.SearchHelper(self.driver).enter_word_Search('iphone 12')
        sleep(3)
        assert page_objects.SearchHelper(self.driver).PAGE_txte_check().text == "Смартфон Apple iPhone 12 64Gb, MGJ73RU/A, (PRODUCT)RED"  # Проверяем, что поиск дал результат
        page_objects.SearchHelper(
            self.driver).click_on_the_favorites_button()  # Добавляем айфон 12 красныйв раздел избранное, нажимаем на кнопку избранное
        page_objects.SearchHelper(
            self.driver).click_on_the_favorites_button2()  # Добавляем айфон 12 белый в раздел избранное, нажимаем на кнопку избранное
        page_objects.SearchHelper(
            self.driver).click_on_the_favorites_button3()  # Добавляем Чехол (футляр) Apple Leather , нажимаем на кнопку избранное
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        iPhones = page_objects.SearchHelper(self.driver).PAGE_txte_check_iPhones()
        assert iPhones.text == '3'  # Проверяем, в разделе избранное находятся три покупки

    @pytest.mark.positive
    def test_editorial_favorites(self):  # Удаление выбранного товара из раздела избранные
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        page_objects.SearchHelper(
            self.driver).click_on_the_favorites_editorial()  # Удаление одного товара из раздела избранное
        sleep(2)
        iPhones = page_objects.SearchHelper(self.driver).PAGE_txte_check_iPhones()
        assert iPhones.text == '2'  # Проверяем, в разделе избранное осталось два товара

    @pytest.mark.positive
    def test_add_in_basket(self):  # Добавляем товары в корзину из избранного
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        page_objects.SearchHelper(self.driver).click_on_the_buy_everything()
        sleep(3)
        page_objects.SearchHelper(self.driver).click_on_the_BUTTON_basket()  # Переходим в корзину
        sleep(5)
        basket = page_objects.SearchHelper(self.driver).txte_check_basket()
        assert basket.text == '2 товара'  # Проверяем, в разделе корзина два товара

    @pytest.mark.positive
    def test_editorial_basket(self):  # Удаление выбранного товара из корзины
        page_objects.SearchHelper(self.driver).click_on_the_BUTTON_basket()
        sleep(3)
        page_objects.SearchHelper(self.driver).click_on_basket_BUTTON_delete()
        sleep(5)
        basket = page_objects.SearchHelper(self.driver).txte_check_basket()
        assert basket.text == '1 товар'  # Проверяем, в разделе корзина один товар

    @pytest.mark.positive
    def test_delete_oll_basket(self):  # Удаление весь товара из корзины
        page_objects.SearchHelper(self.driver).click_on_the_BUTTON_basket()
        sleep(3)
        page_objects.SearchHelper(self.driver).click_on_basket_BUTTON_delete_oll()
        sleep(3)
        basket = page_objects.SearchHelper(self.driver).check_on_basket_delete_oll()
        assert basket.text == 'В корзине нет товаров'  # Проверяем, в разделе корзина нет товаров

    @pytest.mark.positive
    def test_delete_in_favorites(self):  # Удаляем все товары из раздела избранные
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        page_objects.SearchHelper(self.driver).click_on_favorites_BUTTON_oll_delete()
        sleep(3)
        iPhones = page_objects.SearchHelper(self.driver).PAGE_txte_check_iPhones()
        assert iPhones.text != '2'  # Проверяем, в разделе избранное отсутствуют товары

    @pytest.mark.positive
    def test_Search_basket(self):  # Находим товар в поиске и добавляем в корзину
        page_objects.SearchHelper(self.driver).enter_word_Search('iphone 12')
        sleep(3)
        assert page_objects.SearchHelper(
            self.driver).PAGE_txte_check().text == "Смартфон Apple iPhone 12 64Gb, MGJ73RU/A, (PRODUCT)RED"  # Проверяем, что поиск дал результат
        page_objects.SearchHelper(
            self.driver).click_on_the_favorites_basket()  # Добавляем айфон 12 красный в раздел корзина
        sleep(3)
        page_objects.SearchHelper(self.driver).click_on_BUTTON_go_in_basket()
        sleep(3)
        basket = page_objects.SearchHelper(self.driver).txte_check_basket()
        assert basket.text == '1 товар'  # Проверяем, в разделе корзина один товар

    @pytest.mark.positive
    def test_add_from_basket_to_favorites(self):  # Добавление товара из корзины в избранное
        page_objects.SearchHelper(self.driver).click_on_the_BUTTON_basket()
        page_objects.SearchHelper(self.driver).click_on_BUTTON_add_from_basket_to_favorites()
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        iPhones = page_objects.SearchHelper(self.driver).PAGE_txte_check_iPhones()
        sleep(3)
        assert iPhones.text == '1'  # Проверяем, в разделе избранное один товар

    @pytest.mark.positive
    def test_delete1_oll_basket(self):  # Удаление весь товара из корзины
        page_objects.SearchHelper(self.driver).click_on_the_BUTTON_basket()
        sleep(3)
        page_objects.SearchHelper(self.driver).click_on_basket_BUTTON_delete_oll()
        sleep(3)
        basket = page_objects.SearchHelper(self.driver).check_on_basket_delete_oll()
        assert basket.text == 'В корзине нет товаров'  # Проверяем, в разделе корзина нет товаров

    @pytest.mark.positive
    def test_delete1_in_favorites(self):  # Удаляем все товары из раздела избранные
        page_objects.SearchHelper(self.driver).click_on_the_favorites_in_button()
        page_objects.SearchHelper(self.driver).click_on_favorites_BUTTON_oll_delete()
        sleep(3)
        iPhones = page_objects.SearchHelper(self.driver).PAGE_txte_check_iPhones()
        assert iPhones.text != '2'  # Проверяем, в разделе избранное отсутствуют товары


class Test_registration_negative:
    @pytest.mark.negative
    def test_registration_negative_invalid_pass_negative(
            self):  # Проверьте поведение системы при вводе действительного адреса электронной почты и неверного пароля
        page_objects.SearchHelper(self.driver).click_on_the_registration_button()
        # sleep(5)
        page_objects.SearchHelper(self.driver).enter_word_EMAIL('herip@mail.ru')
        # sleep(2)
        page_objects.SearchHelper(self.driver).enter_word_PASS('38743988Zz')
        sleep(4)
        page_objects.SearchHelper(self.driver).click_on_the_registration_COME()
        # sleep(5)
        assert page_objects.SearchHelper(
            self.driver).PAGE_opening_check().text == "Шишин Артем"  # Проверяем, что мы не оказались на главной странице пользователя


    @pytest.mark.negative
    def test_registration_negative_invalid_email_negative(
            self):  # Проверьте поведение системы при вводе неверного идентификатора электронной почты и действительного пароля.
        page_objects.SearchHelper(self.driver).click_on_the_registration_button()
        # sleep(5)
        page_objects.SearchHelper(self.driver).enter_word_EMAIL('herd@mail.ru')
        # sleep(2)
        page_objects.SearchHelper(self.driver).enter_word_PASS('38743988Xx')
        sleep(4)
        page_objects.SearchHelper(self.driver).click_on_the_registration_COME()
        # sleep(5)
        assert page_objects.SearchHelper(
            self.driver).PAGE_opening_check().text == "Шишин Артем"  # Проверяем, что мы не оказались на главной странице пользователя

    @pytest.mark.negative
    def test_registration_negative_invalid_email_and_pass_negative(
            self):  # Проверьте поведение системы при вводе неверного идентификатора электронной почты и действительного пароля.
        page_objects.SearchHelper(self.driver).click_on_the_registration_button()
        # sleep(5)
        page_objects.SearchHelper(self.driver).enter_word_EMAIL('herd@mail.ru')
        # sleep(2)
        page_objects.SearchHelper(self.driver).enter_word_PASS('38743988Xx')
        sleep(4)
        page_objects.SearchHelper(self.driver).click_on_the_registration_COME()
        # sleep(5)
        assert page_objects.SearchHelper(
            self.driver).PAGE_opening_check().text == "Шишин Артем"  # Проверяем, что мы не оказались на главной странице пользователя
