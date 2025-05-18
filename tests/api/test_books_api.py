import requests
import allure

BASE_URL = "https://demoqa.com/BookStore/v1"

@allure.feature("API Book List")
@allure.title("Get all books and check if Git Pocket Guide exists")
def test_get_all_books():
    with allure.step("Отправляем GET-запрос к /Books"):
        response = requests.get(f"{BASE_URL}/Books")

    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200

    with allure.step("Проверяем, что список книг содержит Git Pocket Guide"):
        books = response.json()["books"]
        assert any("Git Pocket Guide" in book["title"] for book in books)
