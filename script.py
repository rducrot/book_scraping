from utils import *
import os.path
import csv
# TODO: use CSV ?

url = 'http://books.toscrape.com/'

books = []

categories = scrap_categories_list(url)

#categories_url_list = ['catalogue/category/books/paranormal_24/index.html']

for category_url, category_name in categories:
    books_url_list = scrap_books_list(url, category_url)

    with open('books/' + category_name.lower() + ".csv", 'w') as file:
        row = ''
        for book_url in books_url_list:
            book = scrap_a_book(book_url)
            for key, value in book.items():
                # TODO: No semi-colon after last value
                row += value + ';'
            file.write(row + '\n')
