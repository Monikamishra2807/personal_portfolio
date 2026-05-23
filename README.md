# Django Portfolio Starter

Production-ready starter for a dynamic personal portfolio built with Django, django-tailwind, HTMX, Alpine.js, PostgreSQL/Supabase, Docker, and Render.

## Included
- Modular Django app architecture
- Dynamic portfolio, projects, experience, education, certifications, and contact models
- DRF endpoints for core content
- Custom dashboard starter
- HTMX form flow examples
- Tailwind warm palette setup
- Docker + Render starter configuration
- Supabase storage service scaffold

## Quick Start
1. Copy `.env.example` to `.env`
2. `docker compose up --build`
3. `python manage.py makemigrations`
4. `python manage.py migrate`
5. `python manage.py createsuperuser`

## Notes
- This is a strong starter codebase, not a fully finished CMS.
- Add forms, auth hardening, tests, and seed data before production.
- Supabase media upload flow is scaffolded through a service class for extension.
