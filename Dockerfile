FROM python:3.12
WORKDIR /app
RUN pip install poetry && poetry config virtualenvs.create false