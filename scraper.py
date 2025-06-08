import requests
from bs4 import BeautifulSoup 
import csv
import re

# Makes script harder to detect as a bot
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    'Accept-Lenguage': 'en-GB,en-US;q=0.9,en;q=0.8,es;q=0.7,ro;q=0.6',
    'Referer': 'https://google.ro/',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive'
}

# Ask for input and request amazon page for that item
url = 'https://www.amazon.com/s?k='
search_item = str(input('What item do you want to search?: '))
response = requests.get(f'{url}{search_item}', headers=headers)

# Parse the page and find all product container
soup = BeautifulSoup(response.text, 'html.parser')
items = soup.find_all('div', class_='sg-col-20-of-24 s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16')

# Loops trough each item 
for item in items:

    # Get the name of item
    name = item.find('h2', class_='a-size-medium a-spacing-none a-color-base a-text-normal')
    
    # Regex pattern to find that exact item and ignore results with "PC" or "Computer" in the name
    pat = search_item.replace(' ', r'\s*')
    if re.search(pat,name.text,re.IGNORECASE) and not re.search('(pc|computer)',name.text,re.IGNORECASE):

        # Get the item price
        simbol = item.find('span', class_='a-price-symbol')
        price = item.find('span', class_='a-price-whole')
        fraction = item.find('span', class_='a-price-fraction')

        # Check if i have all the info i searched for
        if name and simbol and price and fraction:

            # Prints the item + price (optional, for debugging)
            print(f'Product: {name.text} - priced at: {simbol.text}{price.text}{fraction.text}')

            # Saves the data in CSV file
            with open('data.csv','a',newline='') as f:
                writer = csv.DictWriter(f, fieldnames=['item_name','price'])
                writer.writerow({'item_name': name.text,'price': price.text})
        # Else if i dont have all the info i searched for
        else:
            print('One of the fields is missing in this item.')


