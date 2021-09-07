FROM python:3.7 as builder

WORKDIR /usr/src
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry export > requirements.txt


FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src
COPY --from=builder /usr/src/requirements.txt .
RUN pip install -r requirements.txt
