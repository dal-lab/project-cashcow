import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

def crawler(maxpage):
    page = 1
    news = {}

    while page < maxpage:
        # 국민일보의 최신기사 리스트
        url = 'http://www.kmib.co.kr/news/index.asp'
        source_code = requests.get(url, headers=headers)
        # source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        for link in soup.select('dt > a'):
            href = link.get('href')
            # time = soup.find('em', class_='letter')
            news.update({ href : getNews('http://news.kmib.co.kr/article/' + href) })

        page += 1
    
    return news
        
def getNews(href):
    source_code = requests.get(href, headers=headers)
    # source_code = requests.get(href)
    plain_text = source_code.text
    print(plain_text)
    soup = BeautifulSoup(plain_text, 'lxml')
    print(soup)
    content_text = soup.find_all('div', class_='nws_arti')
    print(content_text)
    return content_text

def main():
    news = crawler(2)
    print(news)

main()


    