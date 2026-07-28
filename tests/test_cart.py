from playwright.sync_api import expect

def test_dialog_appears(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    page.get_by_text("Add to Cart").click()
    expect(page.get_by_role("dialog", name="Cart")).to_be_visible()

def test_add_item(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    page.get_by_text("Add to Cart").click()
    cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
    cart_dialog.get_by_role("button", name="Increase quantity").click()
    expect(cart_dialog.get_by_text("2", exact=True)).to_be_visible()

def test_delete_item(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    page.get_by_text("Add to Cart").click()
    page.get_by_label("Remove Drip Coffee Maker 1.5L").click()
    expect(page.get_by_text("Your cart is empty")).to_be_visible()

def test_item_price_consistency(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    product_price = page.locator("span.text-3xl.font-bold.text-gray-900").text_content()
    page.get_by_text("Add to Cart").click()
    cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
    cart_price = cart_dialog.locator("span.text-gray-900").text_content()
    assert product_price == cart_price

def test_item_title_consistency(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    product_title = page.get_by_role("heading", name="Drip Coffee Maker 1.5L").text_content()
    page.get_by_text("Add to Cart").click()
    cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
    cart_title = cart_dialog.get_by_text("Drip Coffee Maker 1.5L").text_content()
    assert product_title == cart_title

def test_item_color_consistency(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    page.get_by_role("button", name="Steel Grey").click()
    product_color = page.get_by_text("Color: Steel Grey").text_content()
    page.get_by_text("Add to Cart").click()
    cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
    cart_color = cart_dialog.get_by_text("Color: Steel Grey").text_content()
    assert product_color == cart_color

def test_cart_to_checkout(page):
    page.goto("https://demo.spreecommerce.org/us/en/products")
    page.get_by_text("Drip Coffee Maker 1.5L").click()
    page.get_by_text("Add to Cart").click()
    cart_dialog = page.get_by_role("dialog").filter(has_text="Cart")
    cart_dialog.get_by_role("link", name="Checkout").click()
    expect(page.get_by_role("button", name="Place Order")).to_be_visible()