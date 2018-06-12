# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:50:20 2018

@author: yyuan1
"""

def split_string(source,splitlist):
    '''Type(source) = string; Type(splitlist) = string, len(splitlist) >= 1'''
    source = [source]
    for item in splitlist:
        source = splitSentencesInListUsingSingleSpliter(source, item)
    return source
        
def split(individule_source, individule_split):
    '''Break a sentence(string) using single split sign (len(indiv_split) = 1)'''
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
    '''Take in a list of sentence(s) and single split sign'''
    result = []
    for sentence in sentenceList:
        result += split(sentence, individule_split)
    return result #A list of sentence free from particular individule_split


out = split_string("This is a test-of the,string separation-code!",",- ")
print(out)

##########################brute-force implementation##########################
def split_string(source, splitlist):
    result = []
    unit = ''
    for letter in source:
        if letter not in splitlist:
            unit += letter
        elif letter in splitlist and unit != '': #second condition to avoid more than 1 space situation ('  ')
            result.append(unit)
            unit = ''
    if unit != '':
        result.append(unit)
    return result

out= split_string("After  the flood   ...  all the colors came out.", " .")
print(out)
assert out == ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
print('Test completed!')
