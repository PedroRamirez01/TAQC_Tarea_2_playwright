
class LoginProcess():
    def __init__ (self, page):
        self.page = page
        self.username = "standard_user"
        self.password = "secret_sauce"
        self.botonLogin = self.page.locator("#login-button")
    
    def login(self) -> None:
        self.page.locator("#user-name").fill(self.username)
        self.page.locator("#password").fill(self.password)
        self.botonLogin.click()

    def logout(self) -> None:
        self.page.locator("#react-burger-menu-btn").click()
        self.page.wait_for_selector("#logout_sidebar_link").click()
