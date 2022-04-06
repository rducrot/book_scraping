import shutil
import csv
from utils import *

images = []

categories = scrap_categories_list()
# categories = [('catalogue/category/books/paranormal_24/index.html', 'Paranormal')]

for category_url, category_name in categories:
    books_url_list = scrap_books_list(category_url)

    with open('books/' + category_name.lower() + ".csv", 'w', newline='') as file:
        writer = csv.DictWriter(file, delimiter=';', fieldnames=FIELDNAMES)
        writer.writeheader()
        for book_url in books_url_list:
            book = scrap_a_book(book_url)
            images.append((book['title'], book['image_url']))
            writer.writerow(book)

for image_title, image_url in images:
    image = requests.get(image_url, stream=True)
    if image.status_code == 200:
        with open('covers/' + image_title.lower().replace(' ', '_') + '.jpg', 'wb') as file:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, file)
