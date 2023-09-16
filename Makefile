mgr:
	python manage.py makemigrations
	python manage.py migrate

run:
	python manage.py runserver localhost:8000
