import shutil
import csv
from utils import *

url = 'http://books.toscrape.com/'
images = []

categories = scrap_categories_list(url)
#categories = [('catalogue/category/books/paranormal_24/index.html', 'Paranormal')]

for category_url, category_name in categories:
    books_url_list = scrap_books_list(url, category_url)

    with open('books/' + category_name.lower() + ".csv", 'w', newline='') as file:
        fieldnames = ['universal_product_code', 'title',
                      'price_including_tax', 'price_excluding_tax',
                      'number_available', 'product_description',
                      'category', 'review_rating', 'image_url']
        writer = csv.DictWriter(file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for book_url in books_url_list:
            book = scrap_a_book(url, book_url)
            images.append((book['title'], book['image_url']))
            writer.writerow(book)

for image_title, image_url in images:
    image = requests.get(image_url, stream=True)
    if image.status_code == 200:
        with open('covers/' + image_title.lower().replace(' ', '_') + '.jpg', 'wb') as file:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, file)
