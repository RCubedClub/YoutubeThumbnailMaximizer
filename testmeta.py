from urllib import urlopen
from bs4 import BeautifulSoup

webpage = urlopen('https://www.youtube.com/watch?v=4Ov_2wNj-bs').read()
soup = BeautifulSoup(webpage, "lxml")

title = soup.find("meta",  property="og:title")
url = soup.find("meta",  property="og:url")

print 'title is '+title["content"]
print 'url is '+url["content"]