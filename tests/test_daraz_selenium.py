from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


"""Test the title of the Daraz Bangladesh website"""
def test_daraz_title(chrome):
    chrome.get("https://www.daraz.com.bd/")
    assert chrome.title == "Online Shopping in Bangladesh: Order Now from Daraz.com.bd"


"""Test the search functionality of the Daraz Bangladesh website"""
def test_daraz_search(chrome):
    url = "https://www.daraz.com.bd/"
    search_term = "Samsung AC"
    chrome.get(url)
    search_box = chrome.find_element(By.ID, value="q")
    search_box.send_keys(search_term + Keys.RETURN)
    assert search_term in chrome.title


"""Test the login functionality of the Daraz Bangladesh website"""
def test_daraz_login(chrome):
    url = "https://member.daraz.com.bd/user/login"
    chrome.get(url)
    email = chrome.find_element(By.CLASS_NAME, "mod-login-input-loginName")
    email.find_element(By.TAG_NAME, 'input').send_keys("test@test.com")
    password = chrome.find_element(By.CLASS_NAME, "mod-login-input-password")
    password.find_element(By.TAG_NAME, 'input').send_keys("testpassword")
    login = chrome.find_element(By.CLASS_NAME, "mod-login-btn")
    login.find_element(By.TAG_NAME, "button").click()

    try:
        logout_button = chrome.find_element(By.CLASS_NAME, "logout")
        assert logout_button.is_displayed(), "Logout button is not displayed."
    except NoSuchElementException:
        assert False, "Logout button does not exist."

    try:
        member_info = chrome.find_element(By.ID, "lzd_current_logon_user_name")
        assert member_info.is_displayed(), "Member info is not displayed."
    except NoSuchElementException:
        assert False, "Member info does not exist."


"""Test the title and description of the Daraz Bangladesh website using the pytest-selenium plugin"""
def test_pytest_selenium_plugin(selenium):
    selenium.implicitly_wait(5)
    selenium.get("https://www.daraz.com.bd/")

    assert selenium.title == "Online Shopping in Bangladesh: Order Now from Daraz.com.bd"

    meta_description = selenium.find_element(By.XPATH, "//meta[@name='description']")
    content_value = meta_description.get_attribute("content")
    expected_content = "Bangladesh's best online shopping store with 17+ million products at resounding discounts in dhaka, ctg & All across Bangladesh with cash on delivery (COD)"
    assert content_value == expected_content
