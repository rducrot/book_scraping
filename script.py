import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

category_url = url + "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"


def scrap_a_book(book_page):
    book_url = url + book_page

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


scrap_a_book('catalogue/the-matchmakers-playbook-wingmen-inc-1_850/index.html')
