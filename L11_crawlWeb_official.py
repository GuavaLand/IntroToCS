# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:55:13 2018

@author: yyuan1
"""
import urllib

def get_page(url):
    f = urllib.request.urlopen(url)
    htmlPage = f.read().decode('utf-8') #https://stackoverflow.com/questions/47056068/python-3-6-typeerror-a-bytes-like-object-is-required-not-str-when-trying-to
    return htmlPage

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"',start_link)
    end_quote = page.find('"',start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url: #False if url = None
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed, max_depth):
    tocrawl = [seed]
    crawled = []
    next_depth = []
    depth = 0
    while tocrawl and depth <= max_depth:
        page = tocrawl.pop()
        if page not in crawled:
            union(next_depth, get_all_links(get_page(page)))
            crawled.append(page)
        if not tocrawl:
            tocrawl, next_depth = next_depth, []
            depth = depth + 1
    return crawled

seed = 'https://udacity.github.io/cs101x/index.html'
crawled = crawl_web(seed, 0)
print(crawled)