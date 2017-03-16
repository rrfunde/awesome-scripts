import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

http = httplib2.Http()
url = 'https://pay.rakuten.co.jp/campaign/invitation/invite.html'

def fetchAndPrint(url):
    status, response = http.request(url)

    for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
        if link.has_key('href'):
            print link['href']
            fetchAndPrint(link['href'])

fetchAndPrint(url)
