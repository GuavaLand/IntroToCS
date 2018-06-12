# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:50:20 2018

@author: yyuan1
"""

def split_string(source,splitlist):
    source = [source]
    for item in splitlist:
        source = splitSentencesInListUsingSingleSpliter(source, item)
    return source
        
def split(individule_source, individule_split):
    result = []
    while True:
        endpos = individule_source.find(individule_split)
        if endpos == -1:
            result.append(individule_source[:])
            break
        result.append(individule_source[: endpos])
        individule_source = individule_source[endpos + 1:]
    return result

def splitSentencesInListUsingSingleSpliter(sentenceList, individule_split):
    result = []
    for sentence in sentenceList:
        result += split(sentence, individule_split)
    return result #A list of sentence free from particular individule_split


out = split_string("This is a test-of the,string separation-code!",",- ")
print(out)