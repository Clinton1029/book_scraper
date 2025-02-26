import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website
BASE_URL = "http://books.toscrape.com/catalogue/"

# Starting URL (Page 1)
page_url = "http://books.toscrape.com/"

# List to store book data
book_list = []

# Rating conversion dictionary
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

while True:
    # Send an HTTP GET request to fetch the page content
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book and extract data
    for book in books:
        title = book.h3.a["title"]
        rating_class = book.p["class"]
        rating = rating_map.get(rating_class[1], "N/A")  # Convert rating text to number
        author = "Not Provided"  # Placeholder for author

        book_list.append({"Title": title, "Author": author, "Rating": rating})

    # Find the "Next" button
    next_page = soup.find("li", class_="next")
    if next_page:
        next_page_url = next_page.a["href"]  # Get relative URL (e.g., "page-2.html")
        page_url = BASE_URL + next_page_url  # Construct full URL
    else:
        break  # No more pages, exit loop

# Convert list to Pandas DataFrame
df = pd.DataFrame(book_list)

# Save data to CSV and Excel
df.to_csv("books.csv", index=False)
df.to_excel("books.xlsx", index=False)

print(f"Scraping complete! {len(df)} books saved to 'books.csv' and 'books.xlsx'.")
