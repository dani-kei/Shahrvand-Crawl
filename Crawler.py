import requests
from bs4 import BeautifulSoup


# Function to crawl a webpage, extract specific data, and save it
def crawl_and_save(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        title = soup.find("h1").get_text()
        div = soup.find("div", class_="single_slideshow_big")
        picURL = div.find("img")
        picURL = picURL["src"]
        barcode = soup.find("div", class_="code change-code").findChildren("span")
        barcode = str(barcode)
        barcode = barcode.removeprefix("[<span>")
        barcode = barcode.removesuffix("</span>]")
        print(title + " : " + barcode + " : "+picURL)
    except:
        pass


# Function to crawl a website and find URLs to crawl
def crawlProductDataWithCategoryUrl(url):
    # Send a GET request to the main page of the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> tags on the page
    a_tags = soup.find_all("a")

    # Extract the URLs from the <a> tags and crawl each URL
    for tag in a_tags:
        try:
            href = tag.get("href")
            if href.startswith("https://shahrvand.ir/fa/product/") and not href.startswith("https://shahrvand.ir/fa/product/cat")  :
              crawl_and_save(href)
        except:
             pass




def crawlCategories(url):
    # Send a GET request to the main page of the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> tags on the page
    a_tags = soup.find_all("a")
    r = ""
    # Extract the URLs from the <a> tags and crawl each URL
    for tag in a_tags:
        try:
            href = tag.get("href")
            if href.startswith("https://shahrvand.ir/fa/product/"):
                r += href
                r += "\n"
            # crawl_and_save(href)
        except:
            pass

    f = open("CategoriesUrl.txt", "w", encoding="utf-8")
    f.writelines(r)
    f.close()
