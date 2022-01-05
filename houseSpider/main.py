from crawler import Crawler
from website import Website

crawler = Crawler()
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com',
     'https://ssearch.oreilly.com/?q=', 'article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content', 'h3.search-result-title a',
     False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu',
     'https://www.brookings.edu/search/?s=',
     'div.list-content article', 'h4.title a', True, 'h1', 'div.post-body']
]


sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2],
                 row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print("GETTING INFO ABOUT: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)

"""
crawler.parse(websites[0], 'http://shop.oreilly.com/product/'
              '0636920028154.do')
crawler.parse(websites[1], 'http://www.reuters.com/article/'
              'us-usa-epa-pruitt-idUSKBN19W2D0')
crawler.parse(websites[2], 'https://www.brookings.edu/blog/'
              'techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/'
              '28/business/energy-environment/oil-boom.html')
"""
