import requests
from bs4 import BeautifulSoup


def scrap_a_book(url, book_url):
    """
    " Return a dictionary of the information of one book
    """
    # TODO:try/except
    page = requests.get(url + book_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return {
        'universal_product_code': soup.find_all('td')[0].text,
        'title': soup.h1.text.replace('/','_'),
        'price_including_tax': soup.find_all('td')[3].text,
        'price_excluding_tax': soup.find_all('td')[2].text,
        # TODO:number_available in int + if 0
        'number_available': soup.find_all('td')[5].text,
        'product_description': soup.find_all('p')[3].text,
        'category': soup.find_all('a')[3].text,
        'review_rating': soup.find_all('p')[2]['class'][1].replace(';', ','),
        'image_url': soup.img['src'].replace('../../', url)
    }


def scrap_books_list(url, category_url):
    """
    " Return a list of the URL of all books of a category
    """
    # TODO: try/except
    page = requests.get(url + category_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Append the soup if there are more than one page of books
    page_number = 2
    next_page_url = url + category_url.replace('index', 'page-' + str(page_number))
    next_page = requests.get(next_page_url)
    while next_page.status_code == 200:
        next_soup = BeautifulSoup(next_page.content, 'html.parser')
        soup.append(next_soup)
        page_number += 1
        next_page_url = url + category_url.replace('index', 'page-' + str(page_number))
        next_page = requests.get(next_page_url)

    book_list_raw = soup.find_all('h3')

    print([book.a['href'].replace('../../../', 'catalogue/') for book in book_list_raw])
    return [book.a['href'].replace('../../../', 'catalogue/') for book in book_list_raw]


def scrap_categories_list(url):
    """
    " Return a list of tuples of the URL and the title of all categories of the site
    """
    # TODO: try/except
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    categories_list_raw = soup.find(class_='nav').find_all('a')
    # Delete the first category as it contains all others categories
    del categories_list_raw[0]
    return [(category['href'], category.text.strip()) for category in categories_list_raw]
