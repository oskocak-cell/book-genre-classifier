import requests, time, os

# genres to fetch
genres = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry": "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html",
    "classics": "http://books.toscrape.com/catalogue/category/books/classics_6/index.html",
    "travel": "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
}

# ensure folder exists
os.makedirs("data/raw", exist_ok=True)

# download & save each genre
for label, url in genres.items():
    filename = f"data/raw/{label}-{time.strftime('%Y%m%d-%H%M%S')}.html"
    resp = requests.get(url)
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"Saved {label} HTML to {filename}")
