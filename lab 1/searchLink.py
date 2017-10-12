from urllib.request import urlopen
import re
from collections import defaultdict
import pickle 
def getLinks(url):
	data = urlopen(url)
	html = str(data.read())
	return re.findall('"((http)s?://.*?)"', html)
def getDomain(domain):
	domainurl= domain.split('.')[1]
	if domainurl.split('.')[0]:
		return domainurl.split('.')[0]
	return domainurl

seedUrl = "https://www.strathmore.edu/"
linksList = []
linksList.append('https://www.strathmore.edu/')
# match anyting after // zero or once
searchLink = defaultdict(list) # store all the links
for val in getLinks(seedUrl):
	if not re.search('.*strathmore.*',val[0]): #
		linksList.append(str(val[0]))

for link in linksList[:]:
	domain = getDomain(link)
	for alink in getLinks(link):
		if not re.search(".*"+domain+".*",alink[0]): #removing links to itself
			searchLink[domain].append(alink[0])
for k, v in searchLink.items():
	print(k,v)