from utils import *

url = 'http://books.toscrape.com/'

books = []

categories_url_list = scrap_categories_list(url)

#categories_url_list = ['catalogue/category/books/paranormal_24/index.html']

for category_url in categories_url_list:
    books_url_list = scrap_books_list(url, category_url)

    for book_url in books_url_list:
        book = scrap_a_book(book_url)
        books.append(book)

[print(book) for book in books]
