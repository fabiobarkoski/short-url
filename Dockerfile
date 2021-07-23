# syntax=docker/dockerfile:1
FROM python:3.9.6-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install uvicorn
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]