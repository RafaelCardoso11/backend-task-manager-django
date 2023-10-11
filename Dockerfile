
FROM python:3.8

ARG EnvironmentVariable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend-django

COPY . .

RUN pip install -r requirements.txt --no-cache-dir
RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]