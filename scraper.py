import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "http://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all quotes
quotes = soup.find_all("span", class_="text")

print("Quotes found:\n")

for quote in quotes:
    print(quote.text)
