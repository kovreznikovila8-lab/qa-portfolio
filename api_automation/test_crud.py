import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1
    assert 'title' in data
    print("✅ GET-тест пройден!")

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    data = {
        "title": "Мой первый пост из Python",
        "body": "Тело поста, написанное скриптом",
        "userId": 1
    }
    response = requests.post(url, json=data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data['title'] == data['title']
    assert 'id' in response_data
    print("✅ POST-тест пройден! id =", response_data['id'])

def test_put_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    updated_data = {
        "id": 1,
        "title": "Обновлённый заголовок через PUT",
        "body": "Новое тело поста, полностью заменённое",
        "userId": 1
    }
    response = requests.put(url, json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == updated_data['title']
    assert data['body'] == updated_data['body']
    print("✅ PUT-тест пройден!")

def test_patch_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    patch_data = {"title": "Новый заголовок через PATCH"}
    response = requests.patch(url, json=patch_data)
    assert response.status_code == 200
    data = response.json()
    assert data['title'] == patch_data['title']
    print("✅ PATCH-тест пройден!")

def test_delete_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    assert response.status_code == 200
    print("✅ DELETE-тест пройден!")