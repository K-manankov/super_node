import requests
import os
import time
import random
import logging
from faker import Faker
import functools

# декоратор повторный попыток
def retry(retries=3):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == retries:
                        raise e
            return func(*args, **kwargs)
        return wrapper
    return decorator_retry

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
@retry(retries=3)
def send_request():
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
    logging.info(f"Ответ: {response.json()}")

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
