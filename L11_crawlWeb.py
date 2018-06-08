# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 10:57:21 2018

@author: yyuan1
"""
import urllib

crawled =[]
TBCrawled = []

def returnHtml(url):
    f = urllib.request.urlopen(url)
    htmlPage = f.read().decode('utf-8') #https://stackoverflow.com/questions/47056068/python-3-6-typeerror-a-bytes-like-object-is-required-not-str-when-trying-to
    return htmlPage

def returnUrl(htmlPage):
    '''Return all url from an HTML page'''
    urlList = []
    while True:
        hrefPos = htmlPage.find('<a href=')
        firstQuote = htmlPage.find('"', hrefPos)
        endQuote = htmlPage.find('"', firstQuote + 1)
        url = htmlPage[firstQuote+1:endQuote]
        if firstQuote != -1:
            urlList.append(url)
            htmlPage = htmlPage[endQuote:]
        else:
            return urlList
            break
    
def exist(lst, target):
    '''Test if target exists in list'''
    if target in lst:
        return True
    else:
        return False
    
def TBCrawledUpdater(urlList):
    for url in urlList: 
        if not exist(crawled, url):
            TBCrawled.append(url)

def crawl_web(seed):
    '''Main method'''
    TBCrawled.append(seed)
    for item in TBCrawled:
        urlList = returnUrl(returnHtml(item))
        crawled.append(item)
        TBCrawledUpdater(urlList)
        
seed = 'https://udacity.github.io/cs101x/index.html'
crawl_web(seed)
print(crawled)