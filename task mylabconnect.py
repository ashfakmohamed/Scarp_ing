import requests
from bs4 import BeautifulSoup
import csv

url = "https://us.princesspolly.com/collections/shoes"

response = requests.get(url)
response.raise_for_status()  
soup = BeautifulSoup(response.content, 'html.parser')
main_box = soup.select_one('.boost-pfs-filter-products')
shoes_data = []
for product_box in main_box.select('.product-tile'):
    image_link = shoe_name = price = 'N/A'
    image_tag = product_box.select_one('.product-tile__media img')
    if image_tag and 'src' in image_tag.attrs:
        image_link = 'https:' + image_tag['src']
    name_tag = product_box.select_one('.product-tile__name')
    shoe_name = name_tag.get_text(strip=True) if name_tag else 'N/A'
    price_tag = product_box.select_one('.product-tile__price')
    price = price_tag.get_text(strip=True) if price_tag else 'N/A'
    shoes_data.append([image_link, shoe_name, price])

csv_file = 'shoes_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Image Link', 'Shoe Name', 'Price'])
    writer.writerows(shoes_data)

print(f"Data has been written to {csv_file}")