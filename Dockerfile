FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY 'yenrwptfe=lh9o_&yzebyy=)3x_&_5t*i)-xewoi59+_!k969$'
ENV DEBUG 1
ENV SQL_ENGINE 'django.db.backends.postgresql'
ENV SQL_DATABASE 'calorie_tracker'
ENV SQL_USER 'luke'
ENV SQL_PASSWORD 'calorie_tracker123'
ENV SQL_HOST 'calorie_tracker_db'
ENV SQL_PORT 5432
ENV DJANGO_SETTINGS_MODULE 'calorie_tracker.settings.development'
ENV DEVELOPMENT_ALLOWED_HOSTS '127.0.0.1, localhost, 0.0.0.0'

RUN mkdir /calorie_tracker_project
WORKDIR /calorie_tracker_project

COPY requirements.txt /calorie_tracker_project/

RUN pip install -r requirements.txt

ADD . /calorie_tracker_project/

# Django service
EXPOSE 8000

