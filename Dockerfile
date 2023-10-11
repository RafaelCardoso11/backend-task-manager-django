
FROM python:3.8

ARG EnvironmentVariable

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /backend-django

COPY . .


RUN pip install --upgrade pip -r requirements.txt --no-cache-dir


EXPOSE 8000

CMD ["gunicorn", "project.wsgi", "--log-file", "0.0.0.0:8000"]