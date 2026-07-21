import requests

# URL для обновления поста с id=1
url = "https://jsonplaceholder.typicode.com/posts/1"

# Новые данные для полной замены (все поля)
updated_data = {
    "id": 1,
    "title": "Обновлённый заголовок через PUT",
    "body": "Новое тело поста, полностью заменённое",
    "userId": 1
}

# Отправляем PUT-запрос
response = requests.put(url, json=updated_data)

# Проверяем статус 200 (успешно)
assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

# Проверяем, что данные обновились
data = response.json()
assert data['title'] == updated_data['title'], "Заголовок не обновился"
assert data['body'] == updated_data['body'], "Тело не обновилось"

print("✅ PUT-тест пройден! Пост полностью обновлён.")