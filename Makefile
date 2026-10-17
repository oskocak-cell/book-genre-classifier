.PHONY: install test run api app docker get-data scrape clean train all

install:
	python -m pip install -r requirements.txt

test:
	python -m pytest -q

run: api

api:
	python -m uvicorn src.api:app --host 0.0.0.0 --port 8000

app:
	python -m streamlit run src/app.py

docker:
	docker build -t book-genre-classifier .

get-data:
	python src/fetch_data.py

scrape:
	python src/scrape_books.py

clean:
	python src/clean_books.py

train:
	python src/classify.py

all:
	$(MAKE) get-data
	$(MAKE) scrape
	$(MAKE) clean
	$(MAKE) train
