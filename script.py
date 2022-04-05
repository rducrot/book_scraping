from utils import *

url = 'http://books.toscrape.com/'

categories_list = scrap_categories_list(url)

for category in categories_list:
    books_list = scrap_books_list(url, category)

    for book in books_list:
        scrap_a_book(book)
