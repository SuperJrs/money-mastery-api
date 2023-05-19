FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

ADD . .

RUN pip install poetry
RUN poetry install

WORKDIR /app/money_mastery/

CMD ["sh", "-c", "poetry run python main.py"]
