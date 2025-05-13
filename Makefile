install:
	pip install -r requirements.txt
lint:
	pylint *.py
format:
	 black *.py
test:
	pytest tests
run:
	flask run

docker-build:
	docker build --tag flask-app .

docker-run:
	docker run -d -p 8080:8080 flask-app
