class SelectProduct:
    def __init__(self, page):
        self.page = page

    def select(self, product_name: str):
        product_locator = self.page.locator(".inventory_item_name", has_text=product_name)
        product_locator.click()
