import requests
import os
import time
import random
import logging
from faker import Faker

# Настройка логирования для вывода в консоль
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# URL и заголовки для запроса
url = os.getenv('TARGET_URL')
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

# Инициализация Faker для генерации случайных вопросов
faker = Faker()

# Функция для отправки запроса
def send_request():
    try:
        # Генерация случайного вопроса с использованием Faker
        question = faker.sentence(nb_words=30)
        # Формирование тела запроса
        data = {
            "messages": [
                {"role": "system", "content": "you're a great rust developer. You need to write an enigma-type encoder that will encode and decode the message transmitted by the user."},
                {"role": "user", "content": question}
            ]
        }
        logging.info(f"Отправка запроса с вопросом: {question}")
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            logging.info(f"Ответ: {response.json()}")
        else:
            logging.error(f"Ошибка получения ответа, статус-код: {response.status_code}")
    except Exception as e:
        logging.error(f"Произошла ошибка при отправке запроса: {str(e)}")

# Основной цикл
def main():
    sleep_hours = 8  # Часы для сна
    sleep_seconds = sleep_hours * 3600  # Перевод в секунды

    while True:
        # Определяем случайное количество запросов перед длинным перерывом
        num_requests = random.randint(6, 12)  # От 6 до 12 запросов (в среднем около часа)

        for _ in range(num_requests):
            send_request()
            # Случайная задержка между запросами от 1 до 5 минут
            delay = random.randint(60, 300)
            logging.info(f"Ожидание {delay // 60} минут...")
            time.sleep(delay)

        # Длинный перерыв от 30 минут до 1 часа
        long_break = random.randint(1800, 3600)
        logging.info(f"Перерыв на {long_break // 60} минут...")
        time.sleep(long_break)

        # Перерыв на сон каждые 24 часа
        logging.info(f"Сон на {sleep_hours} часов...")
        time.sleep(sleep_seconds)

if __name__ == "__main__":
    main()
