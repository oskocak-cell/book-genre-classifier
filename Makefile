#.PHONY: install test run docker

#install:
#	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

test:
	pytest -q

run:
	python -m src

#docker:
	docker build -t my_project .

test:
	pytest -v

get-data:
	python src/fetch_data.py

scrape:
	python src/scrape_books.py

clean:
	python src/clean_books.py   # optional cleaning step

train:
	python src/classify.py

all: get-data scrape train