run:
	flask run
install:
	pip install -r requirements.txt
lint:
	pylint *.py
format:
	 black *.py

