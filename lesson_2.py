import requests
from bs4 import BeautifulSoup
import json

# Function to scrape book data
def scrape_books():
    base_url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    books = []
    
    while base_url:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book containers
        book_containers = soup.find_all('article', class_='product_pod')
        
        for book in book_containers:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text[1:]  # Remove currency symbol
            stock_info = book.find('p', class_='instock availability').text.strip()
            stock_quantity = int(stock_info.split()[2])  # Extract quantity as integer
            
            # Navigate to book detail page for description
            detail_page = book.h3.a['href']
            detail_response = requests.get(f"http://books.toscrape.com{detail_page}")
            detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
            description = detail_soup.find('meta', attrs={'name': 'description'})['content'].strip()

            books.append({
                'title': title,
                'price': float(price),
                'stock': stock_quantity,
                'description': description
            })
        
        # Find the link to the next page
        next_button = soup.find('li', class_='next')
        if next_button:
            next_page = next_button.a['href']
            base_url = f"http://books.toscrape.com/catalogue/category/books_1/{next_page}"
        else:
            base_url = None

    return books

# Save data to JSON file
def save_to_json(data, filename='books.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Main execution
if __name__ == "__main__":
    book_data = scrape_books()
    save_to_json(book_data)