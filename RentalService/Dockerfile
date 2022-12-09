FROM python:3.9


ENV PYTHONUNBUFFERED 1

WORKDIR /app/RentalService

COPY requirements.txt /app/RentalService/requirements.txt

RUN pip install -r requirements.txt

COPY . /app/RentalService


CMD ["sh", "-c", "/usr/local/bin/python RentalService/manage.py makemigrations && /usr/local/bin/python RentalService/manage.py migrate && /usr/local/bin/python RentalService/manage.py runserver 0.0.0.0:8060"]