# Импортируем библиотеку requests, которая умеет отправлять HTTP-запросы
import requests

# URL для создания поста (как в Postman, но без окружения, пишем полный адрес)
url = "https://jsonplaceholder.typicode.com/posts"

# Данные, которые мы отправим (как в Body в Postman)
data = {
    "title": "Мой первый пост из Python",
    "body": "Тело поста, написанное скриптом",
    "userId": 1
}

# Отправляем POST-запрос (как нажатие кнопки Send в Postman)
response = requests.post(url, json=data)

# --- Проверки (как твои тесты во вкладке Tests) ---

# Проверяем статус-код: должен быть 201 (создано)
assert response.status_code == 201, f"Ожидался статус 201, а получили {response.status_code}"

# Преобразуем ответ в JSON, чтобы работать с данными
response_data = response.json()

# Проверяем, что вернулся title, который мы отправили
assert response_data['title'] == data['title'], "Название поста не совпадает"

# Проверяем, что в ответе есть поле id (сервер должен присвоить новый id)
assert 'id' in response_data, "В ответе отсутствует id"

# Если все проверки прошли, выводим сообщение об успехе
print("✅ Тест пройден! Пост создан с id =", response_data['id'])