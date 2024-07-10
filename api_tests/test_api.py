import allure
import requests

BASE_URL = "https://reqres.in/api"


@allure.feature("API Tests")
@allure.story("GET SINGLE USER")
def test_get_single_user():
    response = requests.get(f"{BASE_URL}/users/2")

    with allure.step("Проверяем что код ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверяем что ответ содержит обновленные данные"):
        response_data = response.json()
        assert response_data['data']['id'] == 2
        assert 'email' in response_data['data']
        assert 'first_name' in response_data['data']
        assert 'last_name' in response_data['data']
        print(response.json())

@allure.feature("API Tests")
@allure.story("POST CREATE")
def test_post_create():
    payload = {
        "name": "Тест",
        "job": "Тестер"
    }
    response = requests.post(f"{BASE_URL}/users", data=payload)

    with allure.step("Проверяем что код ответа 201"):
        assert response.status_code == 201

    with allure.step("Проверяем что ответ содержит обновленные данные"):
        response_data = response.json()
        assert response_data['name'] == payload['name']
        assert response_data['job'] == payload['job']
        assert 'id' in response_data
        assert 'createdAt' in response_data
        print(response.json())

@allure.feature("API Tests")
@allure.story("PUT UPDATE")
def test_put_update():
    payload = {
        "name": "Тест Тестович",
        "job": "Тестер"
    }
    response = requests.put(f"{BASE_URL}/users", data=payload)

    with allure.step("Проверяем что код ответа 200"):
        assert response.status_code == 200

    with allure.step("Проверяем что ответ содержит обновленные данные"):
        response_data = response.json()
        assert response_data['name'] == payload['name']
        assert response_data['job'] == payload['job']
        assert 'updatedAt' in response_data
        print(response.json())