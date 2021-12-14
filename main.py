from bs4.element import Tag
import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __init__(self, url) -> None:
        self.__url = url
        self.bs = None

    def change_url(self, url):
        self.__url = url
        self.bs = None

    def get_page_content(self) -> bytes:
        if self.__url is None:
            return None
        r = requests.get(self.__url)
        if r.status_code == 200:
            return r.content
        return None

    def get_value_by_atrribute(self, selector, attribute) -> int:
        self.__parse_page()
        f = self.bs.select_one(selector)
        return f[attribute]

    def get_value_from_text(self, selector) -> int:
        self.__parse_page()
        f = self.bs.select_one(selector)
        return f.string
    
    def __parse_page(self):
        if self.bs is None:
            page = self.get_page_content()
            self.bs = BeautifulSoup(page, 'html.parser')
    

def main():
    url = 'https://www.rebel.pl/promocje/terraformacja-marsa-edycja-gra-roku-99856.html'
    sc = Scrapper(url)
    print('Url:', url)
    val = sc.get_value_by_atrribute('.price[content]', 'content')
    print('Val:', val)

    url = 'https://www.gandalf.com.pl/p/rebel-gra-terraformacja-marsa/'
    sc.change_url(url)
    print('Url:', url)
    print('Val:', sc.get_value_from_text('.internal-price-box > .current-price'))

if __name__ == '__main__':
    main()
        


