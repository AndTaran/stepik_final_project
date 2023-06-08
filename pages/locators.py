# locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс,
# чтобы было удобно импортировать

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')

    NAME_BOOK = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_BOOK = (By.CSS_SELECTOR, '.product_main p.price_color')
    NAME_BOOK_IN_THE_BASKET = (By.CSS_SELECTOR, '.alertinner strong')
    PRICE_BOOK_IN_THE_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
