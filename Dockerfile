FROM python:3.8

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

EXPOSE 8000
