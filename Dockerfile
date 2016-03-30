FROM python:3.5
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt

# move to Django app folder
WORKDIR /code/mysite
