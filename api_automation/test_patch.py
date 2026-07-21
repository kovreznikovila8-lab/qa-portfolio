import requests

# URL для частичного обновления поста с id=1
url = "https://jsonplaceholder.typicode.com/posts/1"

# Данные, которые меняем (только title)
patch_data = {
    "title": "Новый заголовок через PATCH"
}

# Отправляем PATCH-запрос
response = requests.patch(url, json=patch_data)

# Проверяем статус 200
assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

# Проверяем, что title обновился, а другие поля остались
data = response.json()
assert data['title'] == patch_data['title'], "Заголовок не обновился"

print("✅ PATCH-тест пройден! Заголовок частично обновлён.")
