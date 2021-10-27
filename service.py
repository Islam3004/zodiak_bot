import requests
from bs4 import BeautifulSoup

def make_request(goroskop_name):
    url = f"https://uznayvse.ru/goroskop/{goroskop_name}-all-today.html"
    r = requests.get(url)
    return r.content

def get_information(goroskop):
    html = make_request(goroskop)
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('article', id = "maincontent").text
    return divs

   


