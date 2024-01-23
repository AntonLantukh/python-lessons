FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml ./
RUN poetry install

COPY  entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY Makefile uwsgi.ini ./django/ ./
COPY ./django/ ./django

ENTRYPOINT [ "/app/entrypoint.sh" ]