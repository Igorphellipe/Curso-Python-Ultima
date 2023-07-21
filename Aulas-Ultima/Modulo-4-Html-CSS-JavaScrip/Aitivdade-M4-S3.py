#importa a biblioteca HTMLSession da biblioteca resquests_html
from requests_html import HTMLSession
from bs4 import BeautifulSoup

#Cria uma sessão HMTL usando a classe HTMLSession
sessao = HTMLSession()

#define a url da página que será acessada
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

#faz uma requisição GET à página da web usando a sessão criada
resposta = sessao.get(url)

# Usa o metódo di objeto html retornado na resposta para encontrar todos os links dos anúncios
links = resposta.html.find('#ad-list li a')
lista = []
#loop para desmembrar buscas no site
for link in links:
    #extrai o URL de cada anúncio do atributo 'href' do elemento
    url_iphone = link.attrs['href']

    #faz uma requisição GET ao URL de cada anúncio usando a sessão criada
    resposta_iphone = sessao.get(url_iphone)

    if resposta_iphone.status_code == 200:

        #resposta_iphone.html.render()

        pagina = resposta_iphone.html.raw_html

        soup = BeautifulSoup(pagina, 'html.parser')

        titulo = soup.find_all(class_="ad__sc-45jt43-0 htAiPK sc-hSdWYo bYQcLm")
        #for iphone in titulo:
            #print(iphone.text)

        valor = soup.find_all(class_="ad__sc-1wimjbb-1 hoHpcC sc-hSdWYo dDGSHH")
        #for preco in valor:
            #print(preco.text)
        raspagem = {
            'url': url_iphone,
            'titulo': titulo[0].text,
            'valor': valor[0].text,
        }
        lista.append(raspagem)
    else:
        print(f'Falha na requisição{resposta_iphone.status_code}')

for iphones in lista:
    print(iphones)





'''from requests_html import HTMLSession
from bs4 import BeautifulSoup

# URL da página que você deseja fazer a busca
url = "https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone"  # Substitua pela URL real

# Cria uma sessão com o requests_html
session = HTMLSession()

# Faz a requisição HTTP e renderiza o JavaScript (se houver)
response = session.get(url)

# Verifica se a requisição foi bem-sucedida (código de status 200 indica sucesso)
if response.status_code == 200:
    # Renderiza o conteúdo JavaScript (se houver)
    response.html.render()

    # Obtém o conteúdo HTML renderizado da página
    html_content = response.html.raw_html

    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra todos os elementos com a classe "exemplo"
    elementos_exemplo = soup.find_all(class_="exemplo")

    # Itera sobre os elementos encontrados
    for elemento in elementos_exemplo:
        print(elemento.text)
else:
    print(f"Falha na requisição. Código de status: {response.status_code}")
'''