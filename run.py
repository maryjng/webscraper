import requests
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def get_open_html(URL):
    r = requests.get(URL)
    # print(r.status_code)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.get_text())
    return soup

#get each job link from main job search page
def get_joblinks(URL):
    soup = get_open_html(URL)
    links = soup.find_all('a', class_='jobtitle')
    return links

#get relevant info for each link from get_joblinks() and print it
def get_jobinfo(URL):
    links = get_joblinks(URL)
    for job in links:
        print(job.div['jobsearch-DesktopStickyContainer'])
        print(job.find(id="jobDescriptionText"))

get_jobinfo('https://www.indeed.com/jobs?q=Entry+Level+Python&l=New+Jersey')

# div class"jobsearch-SerpJobCard unifiedRow row result clickcard vjs-highlight" #container for each job
# a class="jobtitle turnstileLink visited" #jobtitle
# span class="salaryText" #salary
# span class ="location accessible-contrast-color-location" #location
