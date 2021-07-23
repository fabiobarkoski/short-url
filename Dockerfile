# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8000", "--worker-class", "sanic.worker.GunicornWorker"]