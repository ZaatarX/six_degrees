from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import datetime
import random
import re

pages = set()
random.seed(datetime.datetime.now())

# Retrieves a list of all internal links found on a page


def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme,
                                  urlparse(includeUrl).netloc)
    internalLinks = []

    # find all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*)'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks


def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    # finds all links that start with http that don't contain the current url
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLinks(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one...')
        domain = '{}://{}'.format(urlparse(startingPage).scheme,
                                  urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLinks(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)


followExternalOnly('http://oreilly.com')
