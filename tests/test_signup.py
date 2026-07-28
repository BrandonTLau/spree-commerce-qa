from playwright.sync_api import expect
from pages.demo_spree_login_page import LoginPage
from pages.demo_spree_signup_page import SignUpPage
from faker import Faker

def generate_fake_email():
    fake = Faker()
    unique_email = fake.email()
    return unique_email

def test_navigate_to_sign_up(page):
        login_page = LoginPage(page)
        login_page.goto()

        signup_page = SignUpPage(page)
        signup_page.sign_up_link.click()
        signup_page.expect_on_signup_page()

def test_valid_signup(page):
    unique_email = generate_fake_email()

    login_page = LoginPage(page)
    login_page.goto()

    signup_page = SignUpPage(page)
    signup_page.sign_up_link.click()
    signup_page.enter_first_name("test")
    signup_page.enter_last_name("user")
    signup_page.enter_email(unique_email)
    signup_page.enter_password("testaccount123")
    signup_page.enter_confirm_password("testaccount123")
    signup_page.select_policy_agreement_checkbox()
    signup_page.select_create_account()
    signup_page.expect_signout_button()
    
def test_duplicate_email_signup(page):
    
    login_page = LoginPage(page)
    login_page.goto()
    
    signup_page = SignUpPage(page)
    signup_page.sign_up_link.click()
    signup_page.enter_first_name("test")
    signup_page.enter_last_name("user")
    signup_page.enter_email("janedoe1234@gmail.com")
    signup_page.enter_password("testaccount123")
    signup_page.enter_confirm_password("testaccount123")
    signup_page.select_policy_agreement_checkbox()
    signup_page.select_create_account()
    signup_page.expect_email_taken_alert()


def test_passwords_not_matching(page):
    unique_email = generate_fake_email()
    
    login_page = LoginPage(page)
    login_page.goto()
    
    signup_page = SignUpPage(page)
    signup_page.sign_up_link.click()
    signup_page.enter_first_name("test")
    signup_page.enter_last_name("user")
    signup_page.enter_email(unique_email)
    signup_page.enter_password("testaccount123")
    signup_page.enter_confirm_password("testaccount123456")
    signup_page.select_policy_agreement_checkbox()
    signup_page.select_create_account()
    signup_page.expect_passwords_not_match()

def test_policy_agreement_unchecked(page):
    unique_email = generate_fake_email()
    
    login_page = LoginPage(page)
    login_page.goto()
    
    signup_page = SignUpPage(page)
    signup_page.sign_up_link.click()
    signup_page.enter_first_name("test")
    signup_page.enter_last_name("user")
    signup_page.enter_email(unique_email)
    signup_page.enter_password("testaccount123")
    signup_page.enter_confirm_password("testaccount123")
    signup_page.select_create_account()
    signup_page.expect_policy_agreement_unchecked_message() 