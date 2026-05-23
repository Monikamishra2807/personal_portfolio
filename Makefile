.PHONY: install install-dev sync run migrate migrations superuser shell test lint format collectstatic docker-up docker-down

install:
	uv sync --no-dev

install-dev:
	uv sync --group dev

sync:
	uv sync --group dev

run:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate

migrations:
	uv run python manage.py makemigrations

superuser:
	uv run python manage.py createsuperuser

shell:
	uv run python manage.py shell

test:
	uv run python manage.py test

lint:
	uv run ruff check .

format:
	uv run ruff format .

collectstatic:
	uv run python manage.py collectstatic --noinput

docker-up:
	docker compose up --build

docker-down:
	docker compose down
