from selenium.webdriver.common.by import By

class BooksPage:
    URL = "https://demoqa.com/books"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search_book(self, title):
        search_box = self.driver.find_element(By.ID, "searchBox")
        search_box.clear()
        search_box.send_keys(title)

    def get_search_results(self):
        return self.driver.find_elements(By.CLASS_NAME, "rt-tr-group")