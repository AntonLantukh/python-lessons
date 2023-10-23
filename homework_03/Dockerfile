FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app/

RUN pip install "poetry==1.6.1"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0"]