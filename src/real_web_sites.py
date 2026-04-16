from bs4 import BeautifulSoup
import requests

def find_books():
    html_txt = requests.get('https://books.toscrape.com/catalogue/category/books/romance_8/index.html').text
    soup = BeautifulSoup(html_txt, 'lxml')
    books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

    
    for index, book in enumerate(books):
        book_name = book.find('h3').a['title']
        price = book.find('p', class_ = 'price_color').text
        more_info = book.article.h3.a['href']
        with open(f'posts/{index}.txt', 'w') as post:
            post.write(f"Book name: {book_name}\n")
            post.write(f"Book's price: {price}\n")
            post.write(f"More info: {more_info}\n\n")
        
        print(f"File saved: {index}.txt")
        # print(f"Book name: {book_name}")
        # print(f"Book's price: {price}")
        # print(f"More info: {more_info}")

        # print("")

        # book_description = requests.get('https://books.toscrape.com/catalogue/chase-me-paris-nights-2_977/index.html').text
        # soupd = BeautifulSoup(book_description, 'lxml')
        # page = soupd.find('article', class_ = 'product_page')
        # ps = page.find_all('p')
        # for p in ps:
        #     if len(p.text) > 50:
        #         print(p.text)


if __name__ == '__main__':
    find_books()