import requests
from bs4 import BeautifulSoup


response_example = requests.get('https://coins.bank.gov.ua/pam-jatna-banknota-nominalom-500-griven-zrazka-2015-roku-do-300-richchja-vid-dnja-narodzhennja-grigorija-skovorodi-u-suvenirnij-upakovci-/p-867.html')
response_example2 = requests.get('https://coins.bank.gov.ua/pam-atni-moneti/c-422.html')

soup = BeautifulSoup(response_example.content, 'html.parser')
header = soup.find(class_='category_heading').contents[0].strip()
price = soup.find(class_='new_price_card_product').contents[0]
#quantity = soup.find(class_='category_heading').findNextSibling
quantity = soup.find(class_='col-sm-7 col-xs-12 category-parameters').contents[10].contents[0]

print(header)
print(price)
print(quantity)
soup2 = BeautifulSoup(response_example2.content, 'html.parser')
all_links = soup2.find_all(class_='p_description')
for link in all_links:
    print(link.contents[1].contents[1])


