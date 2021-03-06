#scraping RMS mob data

import requests
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

URLs = ["https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=2",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=3",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=4",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=5",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=6",
        "https://ratemyserver.net/index.php?all_mob_select=%23&mvp=1&nspawn=1&sort_r=0&sort_o=0&page=mob_db&f=1&mob_search=Search&page_num=7"]

def printtotext(text):
    t = open("output1.txt", "a")
    print(text, file=t)
    t.close()

def get_open_html(URL):
    r = requests.get(URL)
    # print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.get_text())
    return soup

def givemobdata(URLs):
    mobdata = {}
    for URL in URLs:
        soup = get_open_html(URL)
        for result in soup.find_all('tr', {'class':'filled_header_mob'}):
            mobname = result.find('th' > 'div').get_text()
            printtotext(mobname)

        for result in soup.find_all('a', {'class':'nbu'}):
            mobmapandtime = result.find_next_siblings('div')
            printtotext(mobmapandtime)

givemobdata(URLs)
