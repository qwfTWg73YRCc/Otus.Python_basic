FROM python:3.8.6-buster

WORKDIR /app

EXPOSE 5000
# install and configure poetry for requirements version control
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY myflaskapp/ ./

CMD ["python", "main.py"]
