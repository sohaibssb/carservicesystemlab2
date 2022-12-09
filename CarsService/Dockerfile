FROM python:3.9


ENV PYTHONUNBUFFERED 1

WORKDIR /app/CarsService

COPY requirements.txt /app/CarsService/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/CarsService


CMD ["sh", "-c", "/usr/local/bin/python CarsService/manage.py makemigrations && /usr/local/bin/python CarsService/manage.py migrate && /usr/local/bin/python CarsService/manage.py runserver 0.0.0.0:8070"]
