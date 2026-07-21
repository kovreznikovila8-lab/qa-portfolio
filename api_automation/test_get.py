import requests

# URL для получения поста с id=1
url = "https://jsonplaceholder.typicode.com/posts/1"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем статус 200 (успешно)
assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

# Проверяем, что в ответе есть поле id и оно равно 1
data = response.json()
assert data['id'] == 1, f"Ожидался id=1, получен {data['id']}"

# Проверяем, что есть поле title
assert 'title' in data, "В ответе нет поля title"

print("✅ GET-тест пройден! Пост с id=1 получен.")