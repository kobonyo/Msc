from urllib.request import urlopen
import re # regex module
seedUrl = "https://www.strathmore.edu/"
linksList = []
linksList.append('https://www.strathmore.edu/')
def getLinks(url): # function to get web content 
	data = urlopen(url)
	html = str(data.read())
	return re.findall('"((http)s?://.*?)"', html) # any http or https link in the page
	                                              # ?-0 or 1, .- match any character,*-repeat 0 or n times

for alink in getLinks(seedUrl):
	if not re.search('.*strathmore.*',alink[0]): # remove links to strathmore page itself
		linksList.append(str(alink[0]))
print(linksList)