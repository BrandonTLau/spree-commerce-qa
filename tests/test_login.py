from playwright.sync_api import expect
from pages.demo_spree_login_page import LoginPage

def test_valid_login_redirects_to_home(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.enter_username("janedoe1234@gmail.com")
    login_page.enter_password("janedoe123")
    login_page.click_login()
    login_page.expect_logged_in()
 

def test_invalid_login_displays_invalid_message(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.enter_username("abc123test@gmail.com")
    login_page.enter_password("abc123test")
    login_page.click_login()
    login_page.expect_invalid_message()

def test_forgot_password_shows_confirmation_message(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.click_forgot_password("janedoe1234@gmail.com")
    login_page.expect_reset_email_confirmation()