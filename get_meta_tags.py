from urllib import urlopen
from bs4 import BeautifulSoup



def extractMetas(url):
	webpage = urlopen(url).read()
	soup = BeautifulSoup(webpage, "lxml")

	title = soup.find("meta",  property="og:title")
	description = soup.find("meta",  property="og:description")

	# print 'title is '+title["content"]
	# print 'description is '+description["content"]

	tags = {'title':title["content"], 'description':description["content"]}

	return tags
