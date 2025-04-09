import requests
from bs4 import BeautifulSoup

urls = [f"https://www.cnblogs.com/#p{i}" for i in range(1,50)]

def craw(url):
    r = requests.get(url)
    
    print(url, len(r.text))

    return r.text

def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text())for link in links]


if __name__ == "__main__":
    for result in parse(craw(urls[2])):
        print(result)
    