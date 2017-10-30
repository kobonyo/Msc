'''
   Set all nodes to "not visited";

   s = new Stack();    ******* Change to use a stack

   s.push(initial node);    ***** Push() stores a value in a stack

   while ( s ≠ empty ) do
   {
      x = s.pop();         ****** Pop() remove a value from the stack

      if ( x has not been visited )
      {
         visited[x] = true;         // Visit node x !

         for ( every edge (x, y)  /* we are using all edges ! */ )    
            if ( y has not been visited )   
           s.push(y);       ***** Use push() !
      }
   }

'''
from urllib.request import urlopen
import re
from collections import defaultdict
import numpy as np 
import requests

def dfs(graph):
    visited = {anode:False for anode in range(len(graph))}
    stack = list()
    stack.append(0)
    while len(stack):
        x = stack.pop()
        if not visited[x]:
            visited[x] = True
            print(x)
            for node in graph:
                for anode in range(len(node)):
                    if not visited[anode]:
                        stack.append(anode)

ROOT_NODE = "https://www.strathmore.edu/"
DEPTH = 10
pagestovisit = getAllLinks(ROOT_NODE)

def pageexists(url):
    request = requests.get(url)
    if request.status_code == 200:
        return True 
    return False 
def getLinks(url):
    if pageexists(url):
        data = urlopen(url)
        html = str(data.read())
        return re.findall('"((http)s?://.*?)"', html)
    return None 

def getAllLinks(node,depth=DEPTH):
    linksList = [] 
    if getLinks(node) and getLinks(node)[:depth]:
        for link in getLinks(node)[:depth]:
            linksList.append(link[0])
    return linksList
def linkoflink():
    searchLink = defaultdict(list)
    links = getAllLinks(ROOT_NODE)
    for link in links:
        pagelinks = getAllLinks(link)
        print(link,'...',pagelinks)
        searchLink[link].append(pagelinks)
    return searchLink

def generatematrix():
    pagestovisit = getAllLinks(ROOT_NODE)
    sourcelinkdict = linkoflink()
    matrix = []
    for source,link in sourcelinkdict.items():
        templist = []
        for alink in pagestovisit:
            if alink in link:
                templist.append(1)
            else:
                templist.append(0)
        matrix.append(templist)
        templist= []
    return matrix
def getwords(url):
    if pageexists(url):
        data = urlopen(url)
        html = str(data.read())
        return re.findall('[A-Za-z0-9\d]+', html)
def removestops(words):
    stopwords = ['a','the','it','at','them','there','is','was','an','he','she','they','them','t','b','\n','n']
    removestops = [word for word in words if word not in stopwords]
    return removestops

def countWords(words):
    wordCount = {}
    for word in words:
        if word in wordCount:
            wordCount[word]+=1
        else:
            wordCount[word] = 1
    return sorted(wordCount.items(), key = itemgetter(1),reverse = True)[:5]

def wordpagefrequency():
    pagewords = defaultdict(list)
    for page in pagestovisit:
        pagewords[page] = getwords(page)
    return pagewords
print(wordpagefrequency())
'''
matrix = generatematrix()
print(matrix)
print('CALLING BFS \n')
print(dfs(matrix))
'''






