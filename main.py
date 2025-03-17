import time
from loginProcess import LoginProcess
from addToCart import AddToCart
from selectProduct import SelectProduct
from playwright.sync_api import sync_playwright

URL = "https://www.saucedemo.com/"

# Context manager
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL, wait_until="domcontentloaded")

    #Login
    login = LoginProcess(page)
    login.login()

    #Select Product
    selectProduct = SelectProduct(page)
    selectProduct.select("Sauce Labs Backpack")

    #Add to Cart
    addToCart = AddToCart(page)
    addToCart.add_to_cart()

    #Verify Cart
    page.locator(".shopping_cart_link").first.click()

    #Logout
    login.logout()
    
    time.sleep(2)
    browser.close()