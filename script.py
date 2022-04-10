import shutil
import csv
from scraping import *

logging.basicConfig(level=logging.INFO)

images = []

# Get a list of tuples of the URL and the name of all categories
categories = scrap_categories_list()
# categories = [('catalogue/category/books/paranormal_24/index.html', 'Paranormal')] # Line for testing

for category_url, category_name in categories:
    # Inform which category is being scraped
    logging.info(CATEGORY_SCRAPING_MESSAGE + category_name)
    # Get a list of URL of all books of the category
    books_url_list = scrap_books_list(category_url)

    # Create a CSV in the 'books/' directory for each category
    with open(RESULT_CSV_FOLDER + category_name.lower() + RESULT_CSV_SUFFIX, 'w', newline=CSV_NEWLINE) as file:
        writer = csv.DictWriter(file, delimiter=CSV_DELIMITER, fieldnames=FIELDNAMES)
        writer.writeheader()
        # Create a line in the CSV for each book
        for book_url in books_url_list:
            # Get a dictionary of every information of the book
            book = scrap_a_book(book_url)
            # Append the 'images' list to download it later
            images.append((book[FIELDNAMES[TITLE_LABEL]], book[FIELDNAMES[IMAGE_URL_LABEL]]))
            writer.writerow(book)

# Inform how many images will be downloaded
logging.info(IMAGE_SCRAPING_MESSAGE.format(len(images)))

# Each image is downloaded in the 'images/' directory
for image_title, image_url in images:
    image = requests.get(image_url, stream=True)
    if image.status_code == 200:
        with open(RESULT_JPG_FOLDER + image_title.lower().replace(' ', '_') + RESULT_JPG_SUFFIX, 'wb') as file:
            image.raw.decode_content = True
            shutil.copyfileobj(image.raw, file)
