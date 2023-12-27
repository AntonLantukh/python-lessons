FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip "poetry==1.6.1"
RUN poetry config virtualenvs.create false --local

COPY poetry.lock pyproject.toml entrypoint.sh gunicorn.conf.py ./

RUN poetry install
RUN chmod +x entrypoint.sh

COPY ./src/ ./

ENTRYPOINT [ "/app/entrypoint.sh" ]