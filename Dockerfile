FROM python:3.12.6-slim

COPY --from=ghcr.io/astral-sh/uv:0.4.8 /uv /bin/uv

WORKDIR /code

COPY ./pyproject.toml .
COPY ./uv.lock .

RUN uv pip install -r pyproject.toml --system

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
