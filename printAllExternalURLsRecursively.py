import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
url = #PUT_URL_HERE

def fetchAndPrint(url):
    status, response = http.request(url)

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            print link['href']
            fetchAndPrint(link['href'])

fetchAndPrint(url)
