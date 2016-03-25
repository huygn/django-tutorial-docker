FROM python:3.5
ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt

# Wait for Postgres ready before starting Django
RUN curl -so /usr/bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /usr/bin/wait-for-it.sh

# move to Django app folder
WORKDIR /code/mysite
