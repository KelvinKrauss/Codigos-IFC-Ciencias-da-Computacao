import requests
from bs4 import BeautifulSoup
URL = "https://quotes.toscrape.com/"
try:
    page = requests.get(URL)
    page.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"NAO DEU PRA PEGA A PAGINA{e}")
    exit()

soup = BeautifulSoup(page.text, 'html.parser')
quotes = soup.find_all('div', class_='quote')

print("--- Scraping Quotes ---")
for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tag_elements = quote.find_all('a', class_='tag')
    tags = [tag.text for tag in tag_elements]
    print(f"quote: {text}")
    print(f"Autor: {author}")
    print(f"Tags: {tags}")
    print("-----------------------------------------------------------------------------------------")