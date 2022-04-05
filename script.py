from utils import *
import shutil
import csv

url = 'http://books.toscrape.com/'
images = []

categories = scrap_categories_list(url)
#categories = [('catalogue/category/books/paranormal_24/index.html', 'Paranormal')]

for category_url, category_name in categories:
    # TODO: if multiple pages (.../cat/page-2.html)
    books_url_list = scrap_books_list(url, category_url)

    with open('books/' + category_name.lower() + ".csv", 'w') as file:
        # TODO : Rewrite using CSV module
        # TODO : Add heading
        for book_url in books_url_list:
            row = ''
            book = scrap_a_book(url, book_url)
            images.append((book['title'], book['image_url']))
            for key, value in book.items():
                row += value + ';'
            file.write(row + '\n')

for image_title, image_url in images:
    image = requests.get(image_url, stream=True)
    if image.status_code == 200:
        with open('covers/' + image_title.lower().replace(' ', '_') + '.jpg', 'wb') as file:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, file)
