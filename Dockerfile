FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY '+zi^y$h9gej3g053r2-dut5t=k4#ez$f6svi6k)1gq7o(vsdnf'
ENV DEBUG 1
ENV SQL_ENGINE 'django.db.backends.postgresql'
ENV SQL_DATABASE 'calorie_tracker'
ENV SQL_USER 'luke'
ENV SQL_PASSWORD 'calorie_tracker123'
ENV SQL_HOST 'calorie_tracker_db'
ENV SQL_PORT 5432
ENV DJANGO_SETTINGS_MODULE 'calorie_tracker.settings.development'
ENV SECRET_ADMIN_URL 'calorie_tracker-admin'
ENV DEVELOPMENT_ALLOWED_HOSTS '127.0.0.1, localhost, 0.0.0.0'
ENV DEVELOPMENT_CORS_ORIGIN_WHITELIST  'http://localhost:4200, http://localhost:8080, http://127.0.0.1:8080, http://localhost:4000'

RUN mkdir /calorie_tracker_project
WORKDIR /calorie_tracker_project

COPY requirements.txt /calorie_tracker_project/

RUN pip install -r requirements.txt

ADD . /calorie_tracker_project/

# Django service
EXPOSE 8000

