import requests
from bs4 import BeautifulSoup

# URL do site alvo
url = https://www.amazon.com.br/Geladeira-Brastemp-Frost-Inverse-litros/dp/B079ZHBWKK?th=1&linkCode=sl1&tag=mfsobrin-20&linkId=03aeba9389b55984d06816dd9fa5316e&language=pt_BR&ref_=as_li_ss_tl

# Enviar uma solicitação GET para o site
response = requests.get(url)

# Verificar se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Obter o conteúdo HTML da página
    html_content = response.content

    # Criar um objeto BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar todas as tags de imagem na página
    img_tags = soup.find_all('img')

    # Extrair as URLs das imagens
    image_urls = [img['src'] for img in img_tags]

    # Imprimir as URLs das imagens
    for img_url in image_urls:
        print(img_url)
else:
    print('Falha ao acessar o site:', response.status_code)
