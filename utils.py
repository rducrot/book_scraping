import requests
from bs4 import BeautifulSoup


def scrap_a_book(url):
    book_url = url

    # TODO:try/catch
    page = requests.get(book_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    book_info = {
        'universal_product_code': soup.find_all('td')[0].text,
        'title': soup.h1.text,
        'price_including_tax': soup.find_all('td')[3].text,
        'price_excluding_tax': soup.find_all('td')[2].text,
        # TODO:number_available in int + if 0
        'number_available': soup.find_all('td')[5].text,
        'product_description': soup.find_all('p')[3].text,
        'category': soup.find_all('a')[3].text,
        'review_rating': soup.find_all('p')[2]['class'][1],
        'image_url': soup.img['src'].replace('../..', url)
    }

    [print(key + ": " + value) for (key, value) in book_info.items()]


def scrap_books_list(url, category):
    category_url = url + category
    # TODO: try/catch
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    book_list_raw = soup.find_all('h3')
    print(book.a['href'].replace('../../../', url + 'catalogue/') for book in book_list_raw)
    return [book.a['href'].replace('../../../', url + 'catalogue/') for book in book_list_raw]


def scrap_categories_list(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    categories_list_raw = soup.find(class_='nav').find_all('a')
    # On supprime la première catégorie qui contient tous les livres
    del categories_list_raw[0]
    return [category['href'] for category in categories_list_raw]
