
class AddToCart:
    def __init__(self, page):
        self.page = page
        self.buttonAddToCart = self.page.locator("#add-to-cart")

    def add_to_cart(self):
        assert self.buttonAddToCart, "No se encontro el botón de agregar al carrito"
        self.buttonAddToCart.click()
