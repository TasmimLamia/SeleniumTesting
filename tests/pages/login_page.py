from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_field = self.driver.find_element(By.CLASS_NAME, "mod-login-input-loginName")
        email_field.find_element(By.TAG_NAME, 'input').send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.CLASS_NAME, "mod-login-input-password")
        password_field.find_element(By.TAG_NAME, 'input').send_keys(password)

    def click_login(self):
        login_field = self.driver.find_element(By.CLASS_NAME, "mod-login-btn")
        login_field.find_element(By.TAG_NAME, "button").click()

    def verify_successful_login(self):
        try:
            logout_button = self.driver.find_element(By.CLASS_NAME, "logout")
            return logout_button.is_displayed()
        except NoSuchElementException:
            assert False, "Logout button does not exist."
