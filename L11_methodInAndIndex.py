# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:33:34 2018

@author: yyuan1
"""

def find_element(lst,target): 
    '''return index of target in lst. If target not present, return -1'''
    #can also use loop to implement. But in and index method make it cleaner
    if target not in lst:
        return -1
    else:
        return lst.index(target)

def test5():
    assert find_element([1,3,5,7],5) == 2
    assert find_element([2,4,6,8],5) == -1
    print('Test5 finished!')
    
test5()
