import pytest

from pages.product_page import ProductPage


@pytest.mark.skip
def test_guest_can_go_to_product(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()


@pytest.mark.skip
@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i == 7, reason='')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.price_and_name_comparison()


# Проверка, что после добавление товара в козину, отсутствует алерт об успешном добавлении товара
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()


# Проверка, что отсутствует алерт об успешном добавлении товара в корзину в КТ
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


# Проверка, что исчезает алерт об успешном добавлении товара в корзину, после добавления в корзину
@pytest.mark.skip
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/studyguide-for-counter-hack-reloaded_205/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
