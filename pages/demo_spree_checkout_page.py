from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page

        self.cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
        self.checkout_link = self.cart_dialog.get_by_role("link", name="Checkout")

        self.email_field = page.get_by_role("textbox", name="Email address")
        self.first_name_field = page.get_by_role("textbox", name="First name")
        self.last_name_field = page.get_by_role("textbox", name="Last name")
        self.address_field = page.get_by_role("textbox", name="Address", exact=True)
        self.city_field = page.get_by_role("textbox", name="City")
        self.state_field = page.get_by_label("State / Province")
        self.zip_field = page.get_by_role("textbox", name="ZIP / Postal code")

        self.premium_shipping_radio = page.get_by_role("radio", name="Premium")

        self.policy_consent_checkbox = page.get_by_role("checkbox", name="I agree to the Privacy Policy")
        self.place_order_button = page.get_by_role("button", name="Place Order")
        self.pay_now_button = page.get_by_role("button", name="Pay Now")

        self.order_confirmation_message = page.get_by_text("Thanks for your order")
        self.order_unsuccessful_message = page.get_by_role("alert").filter(has_text = "Payment was not successful. Please try again.")
     
        self.card_radio = page.get_by_role("radio", name="Stripe")  
        self.affirm_payment_option = page.frame_locator("iframe[title*='payment' i]").first.get_by_test_id("affirm")
        self.authorize_test_payment_button = page.get_by_role("link", name="Authorize Test Payment")  
        self.fail_test_payment_button = page.get_by_role("link", name="Fail Test Payment")  
        self.card_number_field = (
            page.frame_locator("iframe[title*='payment' i]")
            .first
            .locator(".p-CardNumberInput")
            .locator(".p-Input")
            .locator("#payment-numberInput")
        )
        self.expiration_field = (
            page.frame_locator("iframe[title*='payment' i]")
            .first
            .locator("#payment-expiryInput")
        )
        self.cvc_field = (
            page.frame_locator("iframe[title*='payment' i]")
            .first
            .locator("#payment-cvcInput")
        )
        self.card_zip_field = (
            page.frame_locator("iframe[title*='payment' i]")
            .first
            .locator("#payment-postalCodeInput") 
        )
        self.card_declined_message = (
            page.frame_locator("iframe[title*='payment' i]")
            .first
            .get_by_role("alert")
            .filter(has_text="Your card was declined.")
        )

    def expect_card_declined(self):
        expect(self.card_declined_message).to_be_visible(timeout=15000)
    def go_to_checkout(self):
        self.checkout_link.click()

    def fill_shipping_info(self, email, first_name, last_name, address, city, state, zip_code):
        self.email_field.fill(email)
        self.first_name_field.fill(first_name)
        self.last_name_field.fill(last_name)
        self.address_field.fill(address)
        self.city_field.fill(city)
        self.state_field.select_option(state)
        self.zip_field.fill(zip_code)
        self.page.locator("body").click() 

    def select_premium_shipping(self):
        self.premium_shipping_radio.click()

    def accept_policy(self):
        self.policy_consent_checkbox.click()

    def place_order(self):
        self.place_order_button.click()

    def pay_now(self):
        self.pay_now_button.click()

    def expect_order_confirmed(self):
        expect(self.order_confirmation_message).to_be_visible(timeout=15000)

    def expect_order_cancelled(self):
        expect(self.order_unsuccessful_message).to_be_visible(timeout=15000)

    def select_card_payment(self):
        self.card_radio.click()

    def enter_card_details(self, card_number, expiration, cvc, zip_code):
        self.card_number_field.fill(card_number)
        self.expiration_field.fill(expiration)
        self.cvc_field.fill(cvc)
        self.card_zip_field.fill(zip_code)

    def select_affirm(self):
        self.affirm_payment_option.click()

    def click_authorize_test_payment(self):
        self.authorize_test_payment_button.click()

    def click_fail_test_payment(self):
        self.fail_test_payment_button.click()