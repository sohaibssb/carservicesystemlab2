FROM python:3.9


ENV PYTHONUNBUFFERED 1

WORKDIR /app/Gatewayservice

COPY requirements.txt /app/GatewayService/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/GatewayService

CMD ["sh", "-c", " /usr/local/bin/python GatewayService/manage.py makemigrations && /usr/local/bin/python GatewayService/manage.py migrate && /usr/local/bin/python GatewayService/manage.py runserver 0.0.0.0:8080"]
