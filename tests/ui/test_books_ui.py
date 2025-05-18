import time
import pytest
import allure
from pages.books_page import BooksPage

@allure.feature("UI Book Search")
@allure.title("Search for a JavaScript book")
def test_book_search_with_fixture(driver):
    page = BooksPage(driver)

    with allure.step("Открываем страницу книг"):
        page.load()

    with allure.step("Ищем книгу 'JavaScript'"):
        page.search_book("JavaScript")
        time.sleep(2)

    with allure.step("Проверяем, что есть результаты поиска"):
        results = page.get_search_results()
        assert any("JavaScript" in row.text for row in results)
