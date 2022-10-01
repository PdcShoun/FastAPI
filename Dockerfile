FROM python:3.9.0-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

# If python require gcc
# RUN apk add --no-cache --update python3-dev gcc build-base

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
