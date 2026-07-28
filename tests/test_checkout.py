from playwright.sync_api import expect
from pages.demo_spree_checkout_page import CheckoutPage


def add_default_item_to_cart(page):
    page.goto("https://demo.spreecommerce.org/us/en")
    page.get_by_role("link", name="Drip Coffee Maker 1.5L Drip").click()
    page.get_by_role("button", name="Add to Cart").click()


def test_checkout_complete_with_terms(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
        email="janedoe12345@gmail.com",
        first_name="Jane",
        last_name="Doe",
        address="1 Main Street",
        city="San Francisco",
        state="CA",
        zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.accept_policy()
    checkout_page.place_order()
    checkout_page.expect_order_confirmed()

def test_checkout_complete_with_card(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
        email="janedoe12345@gmail.com",
        first_name="Jane",
        last_name="Doe",
        address="1 Main Street",
        city="San Francisco",
        state="CA",
        zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.select_card_payment()
    checkout_page.enter_card_details("4242 4242 4242 4242", "06 / 29", "123", "94116")
    checkout_page.accept_policy()
    checkout_page.pay_now()
    checkout_page.expect_order_confirmed()

def test_checkout_card_declined(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
        email="janedoe12345@gmail.com",
        first_name="Jane",
        last_name="Doe",
        address="1 Main Street",
        city="San Francisco",
        state="CA",
        zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.select_card_payment()
    checkout_page.enter_card_details("4000 0000 0000 0002", "06 / 29", "123", "94116")  
    checkout_page.accept_policy()
    checkout_page.pay_now()
    checkout_page.expect_card_declined()  


def test_checkout_complete_with_affirm(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
        email="janedoe12345@gmail.com",
        first_name="Jane",
        last_name="Doe",
        address="1 Main Street",
        city="San Francisco",
        state="CA",
        zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.select_card_payment()
    checkout_page.select_affirm()
    checkout_page.accept_policy()
    checkout_page.pay_now()

def test_checkout_complete_with_affirm_success(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
            email="janedoe12345@gmail.com",
            first_name="Jane",
            last_name="Doe",
            address="1 Main Street",
            city="San Francisco",
            state="CA",
            zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.select_card_payment()
    checkout_page.select_affirm()
    checkout_page.accept_policy()
    checkout_page.pay_now()
    checkout_page.click_authorize_test_payment()
    checkout_page.expect_order_confirmed()

def test_checkout_complete_with_affirm_failure(page):
    add_default_item_to_cart(page)
    checkout_page = CheckoutPage(page)
    checkout_page.go_to_checkout()
    checkout_page.fill_shipping_info(
            email="janedoe12345@gmail.com",
            first_name="Jane",
            last_name="Doe",
            address="1 Main Street",
            city="San Francisco",
            state="CA",
            zip_code="94116",
    )
    checkout_page.select_premium_shipping()
    checkout_page.select_card_payment()
    checkout_page.select_affirm()
    checkout_page.accept_policy()
    checkout_page.pay_now()
    checkout_page.click_fail_test_payment()
    checkout_page.expect_order_cancelled()