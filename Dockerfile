# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first (better layer caching)
COPY pyproject.toml .python-version ./

# Install production dependencies only (no dev group)
RUN uv sync --frozen --no-dev

# Copy project source
COPY . /app

# Collect static files
RUN mkdir -p /app/staticfiles

# Run with uv-managed Python
CMD ["sh", "-c", \
    "uv run python manage.py migrate && \
     uv run python manage.py collectstatic --noinput && \
     uv run gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 3"]
