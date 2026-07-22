"""
Автотесты для API (CRUD + негативные) на базе JSONPlaceholder.
"""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_post():
    """Проверяем получение поста с id=1."""
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url)
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    data = response.json()
    assert data["id"] == 1, "id поста должен быть равен 1"
    assert "title" in data, "В ответе отсутствует поле title"
    print("✅ GET-тест пройден!")


def test_create_post():
    """Проверяем создание нового поста."""
    url = f"{BASE_URL}/posts"
    payload = {
        "title": "Мой первый пост из Python",
        "body": "Тело поста, написанное скриптом",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
    data = response.json()
    assert data["title"] == payload["title"], "Заголовок не совпадает"
    assert "id" in data, "Ответ не содержит id созданного поста"
    print(f"✅ POST-тест пройден! Новый id = {data['id']}")


def test_put_post():
    """Проверяем полное обновление поста (PUT)."""
    url = f"{BASE_URL}/posts/1"
    updated_data = {
        "id": 1,
        "title": "Обновлённый заголовок через PUT",
        "body": "Новое тело поста, полностью заменённое",
        "userId": 1
    }
    response = requests.put(url, json=updated_data)
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    data = response.json()
    assert data["title"] == updated_data["title"], "Заголовок не обновился"
    assert data["body"] == updated_data["body"], "Тело не обновилось"
    print("✅ PUT-тест пройден!")


def test_patch_post():
    """Проверяем частичное обновление поста (PATCH)."""
    url = f"{BASE_URL}/posts/1"
    patch_data = {"title": "Новый заголовок через PATCH"}
    response = requests.patch(url, json=patch_data)
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    data = response.json()
    assert data["title"] == patch_data["title"], "Заголовок не обновился"
    print("✅ PATCH-тест пройден!")


def test_delete_post():
    """Проверяем удаление поста."""
    url = f"{BASE_URL}/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    print("✅ DELETE-тест пройден!")


def test_get_nonexistent_post():
    """Проверяем, что запрос несуществующего поста возвращает 404."""
    url = f"{BASE_URL}/posts/999"
    response = requests.get(url)
    assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"
    print("✅ Негативный GET-тест пройден (404)")


def test_delete_nonexistent_post():
    """Проверяем, что удаление несуществующего поста не вызывает ошибки (API возвращает 200)."""
    url = f"{BASE_URL}/posts/999"
    response = requests.delete(url)
    # JSONPlaceholder возвращает 200 даже для несуществующих постов
    assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
    print("✅ Негативный DELETE-тест пройден (ожидаем 200 от JSONPlaceholder)")


def test_create_post_without_title():
    """Проверяем, что создание поста без обязательного поля 'title' всё равно работает (специфика API)."""
    url = f"{BASE_URL}/posts"
    payload = {
        "body": "Тело поста без заголовка",
        "userId": 1
    }
    response = requests.post(url, json=payload)
    # JSONPlaceholder создаёт пост даже без title и возвращает 201
    assert response.status_code == 201, f"Ожидался 201, получен {response.status_code}"
    data = response.json()
    assert "id" in data, "В ответе должен быть id созданного поста"
    print("✅ Негативный POST-тест пройден (API позволяет создать пост без заголовка)")
