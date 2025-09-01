import requests, os
from bs4 import BeautifulSoup

url = 'https://www.jaeic.or.jp/smph/shiken/1k/1k-mondai.html'
pdf_link_prefix = 'https://www.jaeic.or.jp/'

save_dir = 'pdfs'
try:
    os.makedirs(save_dir)
except:
    pass

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', href=True)

for link in links:
    if '.pdf' in str(link):
        pdf_url = f'{pdf_link_prefix}{link['href']}'
        pdf_title = pdf_url.rsplit('/')[-1]
        
        resp = requests.get(pdf_url)

        if resp.status_code == 200:
            with open(f'{save_dir}/' + pdf_title, 'wb') as file:
                file.write(resp.content)
            print(f'{pdf_title} downloaded successfully')
        else:
            print(f'Failed to download {pdf_title}')

