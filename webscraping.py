from typing import List, Any

import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.etsy.com/search?q=back+to+school+sign+printable&explicit=1&ref=guided_search_1_1&guided_search=1")
soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

#listings = soup.find(id = "reorderable-listing-results")
#print([item.get_text() for item in listings.select("text-gray-lighter")])


listings = soup.find(id = "reorderable-listing-results")
titles = listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray  ")
#print(titles[0])

#t = [tp.get_text() for tp in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray  ")]
#t = [tp[0] for tp in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray  ")]
listingTitle = []
links= []
#print(listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray  "))

prices = [pz.get_text() for pz in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .n-listing-card__price .currency-value ") ]
testTitle = [tz.get_text() for tz in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray.text-truncate.mb-xs-0.text-body") ]
testPrices = []
#print(listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .n-listing-card__price .currency-value"))

""""
testVar = []
for TL in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .text-gray.text-truncate.mb-xs-0.text-body"):
   testVar.append(TL.get_text())
print("PPPPt",testVar)
"""
#plzhelp = listings.find(class_='strike-through')
#if plzhelp:
#    print(plzhelp)
for pr in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .n-listing-card__price"):
   death = pr.find(class_='strike-through')
   if death:
       print(death)
   else:
       print(pr.get_text())

  """
  # t = pr.find.attrs['aria-label']
  # print(t)
   if pr.get("strike-through"):
       #pr = pr.select(".strike-through .currency-value")
       #testPrices.append(pr.get_text())
       testPrices.append((pr.select(".strike-through .currency-value")))
   else:
       fake = True
       prices2 = [a.get_text() for a in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .n-listing-card__price .currency-value")]
       #pr = listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info .n-listing-card__price .currency-value")
       #text = BeautifulSoup(pr,'html.parser')
       #print(text.get_text())
       #testPrices.append(pr.get_text())
      # testPrices.append((pr.select(".currency-value")))
"""
#testPrices.extend(prices2)

print("LL")
print(testPrices)
print("ZZ")
print("price: ",len(testPrices)," title: ",len(testTitle))



#print(testTitle)

""""
titleHtml = listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression .v2-listing-card__info")
sup = soup(titleHtml, 'lxml')
res = sup.select('text-gray.text-truncate.mb-xs-0.text-body')
print("LLLLLLLLLLLLLLLLLLL", res)
"""




#print("prices: ",prices)

for tp in listings.select(".block-grid-item .js-merch-stash-check-listing .organic-impression"):
   listingTitle.append(tp['title'])
   links.append(tp['href'])
#print(listingTitle)

print(prices)
print((listingTitle))
#print(testTitle)

BTS = pd.DataFrame(
   {
       #"title": listingTitle,
       #"link": links
       "title": testTitle,
       "price": prices

   }
)



print(BTS)


""""
#print(listings.prettify())
#titles = listings.select(".v2-listing-card__info .text-gray text-body")
#print(titles)
listings = soup.find(id = "reorderable-listing-results")
shopNames = listings.select(".v2-listing-card__info .v2-listing-card__shop .text-gray-lighter")
#print(shopNames)
title = shopNames[0]
print(title)
test = title.find(class_="text-gray-lighter")
print("test: ",test)
#print(shopNames[0])
"""

