from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.account_link = page.get_by_label("Account")
        self.email_field = page.locator("#email")
        self.password_field = page.locator("#password")
        self.forgot_password_link = page.get_by_role("link").filter(has_text = "Forgot Password?")
        self.sign_in_button = page.get_by_role("button", name="Sign In")
        self.sign_out_button = page.get_by_role("button", name="Sign Out")
        self.invalid_login_message = page.get_by_role("alert").filter(has_text = "Invalid email or password")
        self.reset_button_link = page.get_by_role("button").filter(has_text="Send reset link")
        self.reset_email_confirmation_message = page.get_by_text("Check your email")
        self.forgot_password_email_field = page.locator("form").filter(has_text = "Reset your password").get_by_placeholder("you@example.com")

    def goto(self):
        self.page.goto("https://demo.spreecommerce.org/us/en")
        self.account_link.click()

    def enter_username(self, email: str):
        self.email_field.fill(email)

    def enter_forgot_password_email(self, email:str):
         self.forgot_password_email_field.fill(email)

    def enter_password(self, password: str):
        self.password_field.fill(password)

    def click_login(self):
        self.sign_in_button.click()

    def click_forgot_password(self, email:str):
        self.forgot_password_link.click()
        self.enter_forgot_password_email(email)
        self.reset_button_link.click()

    def expect_logged_in(self):
        expect(self.sign_out_button).to_be_visible()

    def expect_invalid_message(self):
        expect(self.invalid_login_message).to_be_visible()

    def expect_reset_email_confirmation(self):
        expect(self.reset_email_confirmation_message).to_be_visible()