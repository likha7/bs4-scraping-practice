from bs4 import BeautifulSoup

with open("home.html", 'r') as html_file:
    text = html_file.read()
    
    soup = BeautifulSoup(text, 'lxml')
    #print(soup.prettify())

    titles = soup.find_all('div', class_='product-card')
    
    for title in titles:
        print(title.h3.text.split()[-1])
        price = title.div.span.text
        print(price)

    