FROM python:3.5
ENV PYTHONUNBUFFERED 1

COPY ./apps/requirements.txt /apps/
WORKDIR /apps
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
