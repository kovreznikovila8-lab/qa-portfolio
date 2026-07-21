import requests

# URL для удаления поста с id=1
url = "https://jsonplaceholder.typicode.com/posts/1"

# Отправляем DELETE-запрос
response = requests.delete(url)

# Проверяем статус 200 (или 204, но здесь обычно 200)
assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

print("✅ DELETE-тест пройден! Пост удалён.")
