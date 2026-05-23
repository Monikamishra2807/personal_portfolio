FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev curl && rm -rf /var/lib/apt/lists/*
COPY requirements /app/requirements
RUN pip install --upgrade pip && pip install -r /app/requirements/prod.txt
COPY . /app
RUN mkdir -p /app/staticfiles
CMD ["sh","-c","python manage.py migrate && python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-10000} --workers 3"]
