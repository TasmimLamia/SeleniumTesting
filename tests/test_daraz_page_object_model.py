import pytest
from tests.pages.login_page import LoginPage
from tests.pages.search_page import SearchPage


"""Test the search functionality of the Daraz Bangladesh website"""
@pytest.mark.search
def test_search_pom(chrome):
    url = "https://www.daraz.com.bd/"
    search_term = "Samsung AC"
    search_page = SearchPage(chrome)
    search_page.open_page(url)
    search_page.search(search_term)
    assert search_term in chrome.title


"""Test the login functionality of the Daraz Bangladesh website"""
@pytest.mark.login
def test_login_pom(chrome):
    url = "https://member.daraz.com.bd/user/login"
    login_page = LoginPage(chrome)
    login_page.open_page(url)
    login_page.enter_email("test@test.com")
    login_page.enter_password("testpassword")
    login_page.click_login()
    assert login_page.verify_successful_login()