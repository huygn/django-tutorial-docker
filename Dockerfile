FROM python:3.5
ENV PYTHONUNBUFFERED 1

COPY ./requirements/ /apps/requirements/
COPY requirements.txt /apps/

WORKDIR /apps
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
