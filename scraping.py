import requests
from bs4 import BeautifulSoup
import logging
from constants import *


def scrap_a_book(book_url):
    """
    " Return a dictionary of the information of one book
    """
    try:
        requests.get(URL + book_url)
    except requests.exceptions.ConnectionError:
        logging.error(CONNECTION_ERROR_MESSAGE)
    page = requests.get(URL + book_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return {
        FIELDNAMES[PRODUCT_CODE_LABEL]: soup.find_all('td')[0].text,
        FIELDNAMES[TITLE_LABEL]: soup.h1.text.replace('/', '_'),
        FIELDNAMES[PRICE_INCL_TAX_LABEL]: soup.find_all('td')[3].text,
        FIELDNAMES[PRICE_EXCL_TAX_LABEL]: soup.find_all('td')[2].text,
        FIELDNAMES[STOCK_LABEL]: soup.find_all('td')[5].text,
        FIELDNAMES[DESCRIPTION_LABEL]: soup.find_all('p')[3].text.replace(';', ','),
        FIELDNAMES[CATEGORY_LABEL]: soup.find_all('a')[3].text,
        FIELDNAMES[RATING_LABEL]: soup.find_all('p')[2]['class'][1],
        FIELDNAMES[IMAGE_URL_LABEL]: soup.img['src'].replace('../../', URL)
    }


def scrap_books_list(category_url):
    """
    " Return a list of the URL of all books of a category
    """
    try:
        requests.get(URL + category_url)
    except requests.exceptions.ConnectionError:
        logging.error(CONNECTION_ERROR_MESSAGE)
    page = requests.get(URL + category_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Append the soup if there are more than one page of books
    page_number = 2
    next_page_url = URL + category_url.replace('index', 'page-' + str(page_number))
    next_page = requests.get(next_page_url)
    while next_page.status_code == 200:
        next_soup = BeautifulSoup(next_page.content, 'html.parser')
        soup.append(next_soup)
        page_number += 1
        next_page_url = URL + category_url.replace('index', 'page-' + str(page_number))
        next_page = requests.get(next_page_url)

    book_list_raw = soup.find_all('h3')

    return [book.a['href'].replace('../../../', 'catalogue/') for book in book_list_raw]


def scrap_categories_list():
    """
    " Return a list of tuples of the URL and the title of all categories of the site
    """
    try:
        requests.get(URL)
    except requests.exceptions.ConnectionError:
        logging.error(CONNECTION_ERROR_MESSAGE)

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    categories_list_raw = soup.find(class_='nav').find_all('a')
    # Delete the first category as it contains all others categories
    del categories_list_raw[0]

    return [(category['href'], category.text.strip()) for category in categories_list_raw]
