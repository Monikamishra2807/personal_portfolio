# Django Portfolio Starter

Production-ready personal portfolio built with Django, HTMX, Alpine.js, Tailwind CSS, DRF, PostgreSQL/Supabase, Docker, and deployed via Render.

## Package Management

This project uses **[uv](https://docs.astral.sh/uv/)** — the ultra-fast Python package manager by Astral.

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or via pip
pip install uv
```

## Quick Start (Local)

```bash
# 1. Clone and enter project
git clone https://github.com/Monikamishra2807/personal_portfolio.git
cd personal_portfolio
git checkout development

# 2. Install all dependencies (including dev)
uv sync --group dev

# 3. Copy and fill environment variables
cp .env.example .env

# 4. Run migrations and create superuser
make migrations
make migrate
make superuser

# 5. Start the dev server
make run
```

## Quick Start (Docker)

```bash
cp .env.example .env
docker compose up --build
```

## Common Commands (via Makefile)

| Command | Description |
|---|---|
| `make install-dev` | Install all deps including dev group |
| `make run` | Start Django dev server |
| `make migrate` | Apply migrations |
| `make migrations` | Create new migrations |
| `make superuser` | Create admin user |
| `make shell` | Django shell |
| `make test` | Run tests |
| `make docker-up` | Build and start Docker stack |

## Adding / Removing Packages

```bash
# Add a production dependency
uv add django-debug-toolbar

# Add a dev-only dependency
uv add --group dev pytest-django

# Remove a dependency
uv remove some-package

# Upgrade all packages
uv sync --upgrade
```

## Project Structure

```
personal_portfolio/
├── apps/
│   ├── api/           # DRF serializers and viewsets
│   ├── certifications/
│   ├── common/        # Shared abstract models + Supabase storage service
│   ├── contact/       # Contact form (HTMX)
│   ├── dashboard/     # Admin dashboard (HTMX)
│   ├── education/
│   ├── experience/
│   ├── portfolio/     # Core profile, skills, home view
│   └── projects/
├── config/
│   ├── settings/      # base / local / production
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/         # All HTML templates
├── theme/             # django-tailwind app
├── requirements/      # Legacy pip files (kept for reference)
├── pyproject.toml     # uv project config
├── .python-version    # Pins Python 3.12 for uv
├── Makefile           # Shortcut commands
├── Dockerfile
├── docker-compose.yml
└── .env.example
```

## Notes

- `uv.lock` is gitignored intentionally for a web app — regenerate with `uv sync` on fresh clone.
- Supabase storage upload flow is scaffolded in `apps/common/services/storage.py`.
- Add tests, auth hardening, and seed data before production deployment.
