# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 13:55:13 2018

@author: yyuan1
"""
def get_pages(url):
    #TODO

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

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl: #False if tocrawl = []
        page = tocrawl.pop()
        if page not in crawled:
            links = get_all_links(get_pages(page))
            union(tocrawl, links)
            crawled.append(page)      
    return crawled