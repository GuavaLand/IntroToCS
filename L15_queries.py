# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 16:36:39 2018

@author: yyuan1
"""

#index = [[keyword1,[url1,url2]],[keyword2,[url3]]]

def lookup(index, keyword):
    '''Check if keyword is in index and return url list if so'''
    for item in index:
        if item[0] == keyword:
            return item[1]
    return []

def add_to_index(index, keyword, url):
    '''Add [keyword,[url]] to index'''
    for item in index:
        if keyword == item[0]:
            item[1].append(url)
            return index
    index.append([keyword,[url]])
    return index

def add_page_to_index(index, url, content):
    '''Split content as keyword and add [content.split, [url]] to index'''
    ctntList = content.split()
    for i in ctntList:
        add_to_index(index, i, url)
    return index

index = []
print(add_page_to_index(index,'https://Randy.Pausch',"We cannot change the cards we are dealt, \
                        just how we play the hand. If I don't seem as depressed or morose as I should be, \
                        I'm sorry to disappoint you."))
print(lookup(index,'bad'))
