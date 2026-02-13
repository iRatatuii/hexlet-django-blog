dev:
	uv run manage.py runserver

migrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

shell:
	uv run manage.py shell

create-superuser:
	uv run manage.py createsuperuser

dump:
	uv run manage.py dumpdata > dump.json

lint:
	uv run ruff check --fix