from playwright.sync_api import expect
from pages.demo_spree_login_page import LoginPage

class SignUpPage:
    def __init__(self, page):
        self.page = page 
        self.account_link = page.get_by_label("Account")
        self.sign_up_link = page.get_by_role("link", name = "Sign Up")
        self.first_name_field = page.get_by_label("First name")
        self.last_name_field = page.get_by_label("Last name")
        self.email_field = page.get_by_label("Email")
        self.password_field = page.get_by_role("textbox", name="Password Password", exact=True)
        self.confirm_password_field = page.get_by_role("textbox", name="Confirm Password")
        self.policy_agreement_checkbox = page.get_by_label("I agree to the Privacy Policy and Terms of Service")
        self.create_account_button = page.get_by_role("button", name = "Create Account")
        self.signout_button = page.get_by_role("button", name="Sign Out")
        self.email_taken_alert = page.get_by_role("alert").filter(has_text="Email has already been taken")
        self.passwords_do_not_match_alert = page.get_by_role("alert").filter(has_text="Passwords do not match")
        self.policy_agreement_unchecked_alert = page.get_by_role("alert").filter(has_text="You must agree to the store policies to create an account")

    def click_sign_up_link(self):
        self.sign_up_link.click()

    def enter_first_name(self, fname:str):
        self.first_name_field.fill(fname)

    def enter_last_name(self, lname: str):
        self.last_name_field.fill(lname)

    def enter_email(self, email:str):
        self.email_field.fill(email)

    def enter_password(self, password:str):
        self.password_field.fill(password)

    def enter_confirm_password(self, confirmPassword: str):
        self.confirm_password_field.fill(confirmPassword)

    def select_policy_agreement_checkbox(self):
        self.policy_agreement_checkbox.click()

    def select_create_account(self):
        self.create_account_button.click()

    def expect_signout_button(self):
        expect(self.signout_button).to_be_visible()
        
    def expect_on_signup_page(self):
        expect(self.page).to_have_url("https://demo.spreecommerce.org/us/en/account/register")

    def expect_email_taken_alert(self):
        expect(self.email_taken_alert).to_be_visible()

    def expect_passwords_not_match(self):
        expect(self.passwords_do_not_match_alert).to_be_visible()

    def expect_policy_agreement_unchecked_message(self):
        expect(self.policy_agreement_unchecked_alert).to_be_visible()