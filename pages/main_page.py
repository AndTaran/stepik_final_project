# main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный
# MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
