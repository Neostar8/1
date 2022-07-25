from base import seleniumbase
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from time import sleep

class MainPageLocator:
    LOCATOR_registration_BUTTON= {'by':'css','name':'.js--AuthPopup__button > a > div > div.IconAndTextWithCount__text_mainHeader.IconAndTextWithCount__text'}
    LOCATOR_registration_BUTTON_EMAIL={'by':'xpath', 'name':'//*[@class=" InputBox__input js--InputBox__input  js--SignIn__login__container-input"]'}
    LOCATOR_registration_BUTTON_PASS = {'by': 'CSS','name': 'div.SignIn__password > div > label > input'}
    LOCATOR_registration_BUTTON_COME = {'by': 'CSS', 'name': 'div.SignIn__actions > div.SignIn__action.SignIn__action_sign-in > button'}
    LOCATOR_PAGE_opening_check = {'by': 'CSS', 'name': 'div.HeaderUserName__name'}
    LOCATOR_BUTTON_Search = {'by': 'CSS','name': '.MainHeader__search > div > div > form > div > div.SearchQuickResult__input-wrapper > div > label > input'}
    LOCATOR_TXTE_check = {'by': 'xpath','name':'//*[@title="Смартфон Apple iPhone 12 64Gb,  MGJ73RU/A,  (PRODUCT)RED"]'}
    LOCATOR_BUTTON_favorites = {'by': 'CSS', 'name':'div:nth-child(1) >div > div.ProductCardVerticalLayout__footer > div.ProductCardVerticalLayout__wrapper-actions > div > div:nth-child(1) > div > label > span > svg'}
    LOCATOR_BUTTON_favorites2 = {'by': 'CSS', 'name':'div:nth-child(3) > div > div.ProductCardVerticalLayout__footer > div.ProductCardVerticalLayout__wrapper-actions > div > div:nth-child(1) > div > label > span > svg'}
    LOCATOR_BUTTON_favorites3 = {'by': 'CSS', 'name':'div:nth-child(2) > div > div.ProductCardVerticalLayout__footer > div.ProductCardVerticalLayout__wrapper-actions > div > div:nth-child(1) > div > label > span > svg'}
    LOCATOR_TXTE_check_iPhones= {'by': 'CSS', 'name':'body > div.MainWrapper > div.MainLayout.js--MainLayout.HeaderFixer > header > div.Container.Container_has-grid.MainHeader__inner.MainHeader__inner_bottom.js--MainHeader__inner_bottom > div.MainHeader__actions-block.md-col-start-2.row-start-1.md-col3.xs-col3.ml-col4 > div.HeaderMenu.js--HeaderMenuMobile > div.HeaderMenu__buttons-wrapper > div.HeaderMenu__buttons.HeaderMenu__buttons_wishlist > a > div > div.IconAndTextWithCount__icon_mainHeader.IconAndTextWithCount__icon.js--IconAndTextWithCount__icon > div'}
    LOCATOR_BUTTON_favorites4 = {'by': 'CSS', 'name':'div.HeaderMenu__buttons.HeaderMenu__buttons_wishlist > a > div > div.IconAndTextWithCount__text_mainHeader.IconAndTextWithCount__text'}
    LOCATOR_editorial_favorites = {'by': 'CSS', 'name':'div:nth-child(3) > div > div.ProductCardVerticalLayout__footer > div.ProductCardVerticalLayout__wrapper-actions > div > div:nth-child(1) > label.js--RemoveFromWishlist.ProductListFavourites__wishlist.js--RemoveFromWishlist.ProductListFavourites__wishlist_desktop.ProductCardButton.js--ProductCardButton > span > svg'}
    LOCATOR_favorites_BUTTON_buy_everything = {'by': 'xpath', 'name':'//*[@data-label="Купить все товары"]'}
    LOCATOR_BUTTON_basket= {'by': 'CSS', 'name':'div.HeaderMenu__buttons.HeaderMenu__buttons_basket > a > div'}
    LOCATOR_basket_check = {'by': 'CSS','name':'div.OrderFinalPrice__order-count'}
    LOCATOR_favorites_BUTTON_oll_delete = {'by':'xpath', 'name': '//*[@data-label="Очистить список"]'}
    LOCATOR_basket_BUTTON_delete = {'by':'CSS', 'name':'div:nth-child(1) > div.product_data__gtm-js.product_data__pageevents-js.js--ProductCardForBasket.ProductCardForBasket > div.ProductCardForBasket__inner > div.ProductCardForBasket__icons > div:nth-child(2) > svg'}
    LOCATOR_basket_BUTTON_delete_oll = {'by':'xpath','name':'//*[@data-label="Очистить корзину"]'}
    LOCATOR_basket_check_delete = {'by':'xpath','name':'//*[@class="Basket__basket-empty-title"]'}
    LOCATOR_BUTTON_basket_buy = {'by': 'CSS', 'name':'div:nth-child(1) > div > div.ProductCardVerticalLayout__footer > div.ProductCardVerticalLayout__wrapper-cart > div > div.Hint.ProductCardVerticalCart__button-add-hint.js--Hint.js--Hint_hover.Hint_placement_right > button > span > span'}
    LOCATOR_BUTTON_go_in_basket = {'by': 'CSS','name':'.UpsaleBasket__header > div > div:nth-child(2) > button > span'}
    LOCATOR_BUTTON_add_from_basket_to_favorites = {'by':'xpath','name':'//*[@data-label="Добавить все в избранное"]'}


class SearchHelper(seleniumbase.SeleniumBase):
        def __init__(self, driver):
            super().__init__(driver)

        def click_on_the_registration_button(self):
            registration_field = self.is_present(MainPageLocator.LOCATOR_registration_BUTTON['by'],MainPageLocator.LOCATOR_registration_BUTTON['name'])
            registration_field .click()
            return registration_field

        def enter_word_EMAIL(self, word: str) ->WebElement:
            EMAIL_field = self.is_present(MainPageLocator.LOCATOR_registration_BUTTON_EMAIL['by'], MainPageLocator.LOCATOR_registration_BUTTON_EMAIL['name'])
            EMAIL_field.click()
            EMAIL_field.send_keys(word) # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
            return EMAIL_field

        def enter_word_PASS(self, word: str) ->WebElement:
            PASS_field = self.is_present(MainPageLocator.LOCATOR_registration_BUTTON_PASS['by'], MainPageLocator.LOCATOR_registration_BUTTON_PASS['name'])
            PASS_field.send_keys(word) # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
            return PASS_field

        def click_on_the_registration_COME(self):
            COME_field = self.is_present(MainPageLocator.LOCATOR_registration_BUTTON_COME['by'],MainPageLocator.LOCATOR_registration_BUTTON_COME['name'])
            COME_field.click()
            return COME_field

        def PAGE_opening_check(self):
            opening_check = self.is_present(MainPageLocator.LOCATOR_PAGE_opening_check['by'],MainPageLocator.LOCATOR_PAGE_opening_check['name'])
            return opening_check

        def enter_word_Search(self, word: str) ->WebElement:
            PASS_field = self.is_present(MainPageLocator.LOCATOR_BUTTON_Search['by'], MainPageLocator.LOCATOR_BUTTON_Search['name'])
            PASS_field.send_keys(word, Keys.ENTER) # (word, Keys.ENTER) Keys.RETURN-Нажать Enter
            return PASS_field

        def PAGE_txte_check(self):
            opening_txte = self.is_present(MainPageLocator.LOCATOR_TXTE_check['by'],MainPageLocator.LOCATOR_TXTE_check['name'])
            return opening_txte

        def click_on_the_favorites_button(self):
            favorites_button = self.is_present(MainPageLocator.LOCATOR_BUTTON_favorites['by'],MainPageLocator.LOCATOR_BUTTON_favorites['name'])
            favorites_button.click()
            return favorites_button

        def click_on_the_favorites_button2(self):
            favorites_button2 = self.is_present(MainPageLocator.LOCATOR_BUTTON_favorites2['by'],MainPageLocator.LOCATOR_BUTTON_favorites2['name'])
            favorites_button2.click()
            return favorites_button2

        def click_on_the_favorites_button3(self):
            favorites_button3 = self.is_present(MainPageLocator.LOCATOR_BUTTON_favorites3['by'],MainPageLocator.LOCATOR_BUTTON_favorites3['name'])
            favorites_button3.click()
            return favorites_button3

        def PAGE_txte_check_iPhones(self):
            opening_txte_iPhones = self.is_present(MainPageLocator.LOCATOR_TXTE_check_iPhones['by'],MainPageLocator.LOCATOR_TXTE_check_iPhones['name'])
            return opening_txte_iPhones

        def click_on_the_favorites_in_button(self):
            favorites_button4 = self.is_present(MainPageLocator.LOCATOR_BUTTON_favorites4['by'],MainPageLocator.LOCATOR_BUTTON_favorites4['name'])
            favorites_button4.click()
            return favorites_button4

        def click_on_the_favorites_editorial(self):
            editorial_favorites_button4 = self.is_present(MainPageLocator.LOCATOR_editorial_favorites['by'],MainPageLocator.LOCATOR_editorial_favorites['name'])
            editorial_favorites_button4.click()
            return editorial_favorites_button4

        def click_on_the_buy_everything(self):
            buy_everything = self.is_present(MainPageLocator.LOCATOR_favorites_BUTTON_buy_everything['by'],MainPageLocator.LOCATOR_favorites_BUTTON_buy_everything['name'])
            buy_everything.click()
            return buy_everything

        def click_on_the_BUTTON_basket(self):
            BUTTON_basket = self.is_present(MainPageLocator.LOCATOR_BUTTON_basket['by'],MainPageLocator.LOCATOR_BUTTON_basket['name'])
            BUTTON_basket.click()
            return BUTTON_basket

        def txte_check_basket(self):
            opening_txte_iPhones = self.is_present(MainPageLocator.LOCATOR_basket_check['by'],MainPageLocator.LOCATOR_basket_check['name'])
            return opening_txte_iPhones

        def click_on_favorites_BUTTON_oll_delete(self):
            oll_delete = self.is_present(MainPageLocator.LOCATOR_favorites_BUTTON_oll_delete['by'],MainPageLocator.LOCATOR_favorites_BUTTON_oll_delete['name'])
            oll_delete.click()
            return oll_delete

        def click_on_basket_BUTTON_delete(self):
            basket_BUTTON_delete = self.is_present(MainPageLocator.LOCATOR_basket_BUTTON_delete['by'],MainPageLocator.LOCATOR_basket_BUTTON_delete['name'])
            basket_BUTTON_delete.click()
            return basket_BUTTON_delete

        def click_on_basket_BUTTON_delete_oll(self):
            basket_BUTTON_delete_oll = self.is_present(MainPageLocator.LOCATOR_basket_BUTTON_delete_oll['by'],MainPageLocator.LOCATOR_basket_BUTTON_delete_oll['name'])
            basket_BUTTON_delete_oll.click()
            return basket_BUTTON_delete_oll

        def check_on_basket_delete_oll(self):
            basket_BUTTON_delete_oll = self.is_present(MainPageLocator.LOCATOR_basket_check_delete['by'],MainPageLocator.LOCATOR_basket_check_delete['name'])
            basket_BUTTON_delete_oll.click()
            return basket_BUTTON_delete_oll

        def click_on_the_favorites_basket(self):
            favorites_basket = self.is_present(MainPageLocator. LOCATOR_BUTTON_basket_buy['by'],MainPageLocator. LOCATOR_BUTTON_basket_buy['name'])
            favorites_basket.click()
            return favorites_basket

        def click_on_BUTTON_go_in_basket(self):
            go_in_basket = self.is_present(MainPageLocator. LOCATOR_BUTTON_go_in_basket['by'],MainPageLocator. LOCATOR_BUTTON_go_in_basket['name'])
            go_in_basket.click()
            return go_in_basket

        def click_on_BUTTON_add_from_basket_to_favorites(self):
            go_in_basket = self.is_present(MainPageLocator. LOCATOR_BUTTON_add_from_basket_to_favorites['by'],MainPageLocator. LOCATOR_BUTTON_add_from_basket_to_favorites['name'])
            go_in_basket.click()
            return go_in_basket
