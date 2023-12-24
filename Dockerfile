
# образ на основе которого создаём контейнер
FROM python:3.8

# рабочая директория внутри проекта
WORKDIR /code

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
RUN pip install --upgrade pip

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]