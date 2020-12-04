import requests
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

#print to txt
def print_to_text(txt, txtfile):
    t = open(txtfile, "a")
    print(txt, file=t)
    t.close()  
    
#get soup
def get_open_html(URL):
    r = requests.get(URL)
    # print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.get_text())
    return soup

#prettify soup
def prettify(soup):
    return soup.prettify()  

#get each link from soup using class and <a>
def get_links(URL):
    soup = get_open_html(URL)
    links = soup.find_all('a', class_='<INSERT CLASSS>')
    return links

#print text within tags filtered by class and CSS selector
def findall_filter(URL):
    soup = get_open_html(URL)
    for result in soup.find_all('<TAG>', {'class':'<INSERT CLASS>'}):
        item = result.find('<TAG1>' > '<TAG2>').get_text()
        printtotext(item)

get_jobinfo('<URL>')
