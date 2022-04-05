import requests
from bs4 import BeautifulSoup


def scrap_a_book(url):
    """
    " Scrap all the information of one book
    """
    # TODO:try/catch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return {
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


def scrap_books_list(url, category_url):
    """
    " Scrap the URL of all books of a category
    """
    # TODO: try/catch
    page = requests.get(url + category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    book_list_raw = soup.find_all('h3')
    return [book.a['href'].replace('../../../', url + 'catalogue/') for book in book_list_raw]


def scrap_categories_list(url):
    """
    " Scrap the URL of all the categories of the site
    """
    # TODO: try/catch
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    categories_list_raw = soup.find(class_='nav').find_all('a')
    # On supprime la première catégorie qui contient toutes les autres catégories
    del categories_list_raw[0]
    return [(category['href'], category.text.strip()) for category in categories_list_raw]
