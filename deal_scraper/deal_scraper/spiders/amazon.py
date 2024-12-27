import requests
from lxml import html

BASE_URL = "https://www.amazon.com"

def scrape_amazon():
    url = "https://www.amazon.com/s?k=graphics+card"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)

    # Parse the response
    tree = html.fromstring(response.content)

    # Extract data
    products = []
    for product in tree.xpath('//div[@data-cy="title-recipe"]'):
        try:
            # Product name
            name = product.xpath('.//h2/span/text()')[0]
            # Product link
            partial_href = product.xpath('./a[@class="a-link-normal"]/@href')[0]
            link = BASE_URL + partial_href
            # Product price
            price = product.xpath('.//span[@class="a-offscreen"]/text()')[0]

            # Add to product list
            products.append({"name": name, "price": price, "link": link})
        except IndexError:
            # Skip products with missing data
            continue

    return products

# Test the scraper
deals = scrape_amazon()
for deal in deals:
    print(deal)
