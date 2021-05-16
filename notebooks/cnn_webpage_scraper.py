
## This is a simple Webpage Scraper of the news website CNN

# Step 0: Necessary Library Imports

import requests
from bs4 import BeautifulSoup
import sys

#------------------------------------------------------------------------
# Step 1: Function- Download the webpage
def download_webpage(url):
    """ This function   downloads the HTML script of the given webpage"""
    webpage = requests.get(url)

    if (webpage.ok == True): # status_code check
        print("Hurray! Webpage found and downloaded successfully!")
    else:
        print("Incorrect URL! please verify and try again!")

    page_content = webpage.content
    
    webpage.close()

    return page_content

#------------------------------------------------------------------------
# Step 2: Copy url from script argument and execute the above function to download the webpage

if len(sys.argv) > 1:
    page = str(sys.argv[2])
    print(f"Looking up the url {page}")
else:
    page = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"
    print(f"No URL was given. We will scrap the example news webpage {page}")

    
webpage_html = download_webpage(page)

#------------------------------------------------------------------------
# Step 3: Find Article Title, Author, Date and Content
soup = BeautifulSoup(webpage_html, 'html.parser')

## Item 1: News article headline
news_article_title = soup.find_all("h1", {"class": "Article__title"})[0].text

## Item 2: News article author
news_article_author = soup.find_all("div", {"class": "Article__subtitle"})[0].text
news_article_author = news_article_author.split('•')[0].split(',')[0]

## Item 3: News article published/last updated date
news_article_date = soup.find_all("div", {"class": "Article__subtitle"})[0].text
news_article_date = news_article_date.split('•')[1][9:]

print(f"Article Title: {news_article_title}" + f"\nArticle Author:{news_article_author}" + f"\nArticle Published/last updated date:{news_article_date}")

#------------------------------------------------------------------------
## Item 4: Article body
news_article_content = soup.find_all("div", {"class": "Article__content"})[0].text
news_article_content = news_article_content.split('(CNN) — ')[1]

# print the news article body
print("\n\nNews Content:\n\n")
for line in news_article_content.split('\n'):
    print(line)

print("\n\nEnd of News!Ciao")

#------------------------------------------------------------------------