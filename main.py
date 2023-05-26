
import Crawler

#first crawl Categories Page with this function
Crawler.crawlCategories()

#then append some variable to the end of categories url to get all product in each page.
#then store it in ProductListUrl
#now  wanna to crawl this Urls to get data

f = open("ProductListUrl.txt","r",encoding="utf-8")
urls = f.readlines()
for u in urls:
    Crawler.crawlProductDataWithCategoryUrl(u)





