# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Устанавливаем зависимости
RUN pip install requests --no-cache-dir &&\
pip install faker --no-cache-dir

# Копируем ваш Python скрипт в контейнер
COPY requests_generator.py .

# Указываем команду, которая будет выполнена при запуске контейнера
CMD ["python", "requests_generator.py"]
