import requests
from bs4 import BeautifulSoup

def enter-URL(URL):
  page = requests.get(URL)
  
  soup = BeautifulSoup(page.content, 'html.parser')

def find-ID(ID):
  results = soup.find(id=ID)
  print(results.prettify())
  
def find-class(section, classname):
  results = results.findall(section, class_ = 'classname')
  
  for results in results:
  print(result, end='\n'*2)
  #each result is an object that can use .find(tag, class) and .text
