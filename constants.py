# URL of the site to scrap
URL = 'http://books.toscrape.com/'

# Fieldnames used in the CSV
FIELDNAMES = ['universal_product_code', 'title',
              'price_including_tax', 'price_excluding_tax',
              'number_available', 'product_description',
              'category', 'review_rating', 'image_url']
# Labels for the FIELDNAMES list
PRODUCT_CODE_LABEL = 0
TITLE_LABEL = 1
PRICE_INCL_TAX_LABEL = 2
PRICE_EXCL_TAX_LABEL = 3
STOCK_LABEL = 4
DESCRIPTION_LABEL = 5
CATEGORY_LABEL = 6
RATING_LABEL = 7
IMAGE_URL_LABEL = 8

# CSV parameters
RESULT_CSV_FOLDER = 'books/'
RESULT_CSV_SUFFIX = '.csv'
CSV_DELIMITER = ';'
CSV_NEWLINE = ''

# JPG parameters
RESULT_JPG_FOLDER = 'covers/'
RESULT_JPG_SUFFIX = '.jpg'

# LOGGER MESSAGES
# Scraping books from categories information
CATEGORY_SCRAPING_MESSAGE = 'Scraping books of category '
# Number of images scraped
IMAGE_SCRAPING_MESSAGE = 'Downloading {} images'
# Error log when connection error
CONNECTION_ERROR_MESSAGE = 'No connection to the website'
