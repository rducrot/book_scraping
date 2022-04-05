from utils import *
import os.path
import csv
# TODO: use CSV ?

url = 'http://books.toscrape.com/'

categories = scrap_categories_list(url)

#categories_url_list = ['catalogue/category/books/paranormal_24/index.html']

for category_url, category_name in categories:
    # TODO: if multiple pages (.../cat/page-2.html)
    books_url_list = scrap_books_list(url, category_url)

    with open('books/' + category_name.lower() + ".csv", 'w') as file:
        for book_url in books_url_list:
            row = ''
            book = scrap_a_book(book_url)
            for key, value in book.items():
                # TODO: No semi-colon after last value
                # TODO: Correct problems with ';' in some text descriptions
                row += value + ';'
            file.write(row + '\n')
