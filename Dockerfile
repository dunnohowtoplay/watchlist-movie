FROM python:3.9

WORKDIR /code

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./main.py /code/
COPY ./alembic /code/alembic
COPY .env /code/.env
COPY alembic.ini /code/

EXPOSE 8000

