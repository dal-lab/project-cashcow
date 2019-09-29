import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def crawler(maxpage):
    page = 1
    news = {}

    while page < maxpage:
        # 경향신문의 최신기사 리스트
        url = 'http://news.khan.co.kr/kh_recent/index.html?&page=' + str(page)
        source_code = requests.get(url, headers=headers)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        for link in soup.select('strong > a'):
            href = link.get('href')
            # time = soup.find('em', class_='letter')
            news.update({ href : getNews('http:' + href) })

        page += 1
    
    return news
        
def getNews(href):
    source_code = requests.get(href, headers=headers)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    content_text = soup.find_all('p', class_ = 'content_text')
    # print(content_text)
    return content_text

def main():
    news = crawler(2)
    print(news)

main()


    