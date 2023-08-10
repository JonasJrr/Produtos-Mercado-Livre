import requests
from bs4 import BeautifulSoup

entrada = input("Digite aqui o que você deseja pesquisar no Mercado Livre:")

url = "https://lista.mercadolivre.com.br/{}".format(entrada).replace(" ", "-")

requisicao = requests.get(url)

response = requisicao.content
soup = BeautifulSoup(response, 'html.parser')

resultado = soup.find_all(class_='ui-search-item__title shops__item-title') 

for itens in resultado:
    print(itens.text)



