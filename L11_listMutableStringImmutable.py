# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 09:32:21 2018

@author: yyuan1
"""
import os
os.chdir('C:\Sources\IntroToCS')

p = [1,2]
q = [3,4]
p.append(q) #Append modifies on the original list
def test1():
    assert len(p) == 3
    print('Test1 finished!')
    
test1()

q[1] = 5

def test2():
    assert p == [1,2,[3,5]] #3rd element of p is q. B/c list is mutable, change q does not change p's reference to q,
                            #so p's value is also changed
    print('Test2 finished!')
    
test2()

def changeListValue(lst):
    lst[0] = 'Changed' #list is mutable so local variable lst value change, whichever variable refering to the same
                       #list has its value changed
    
def test3():
    changeListValue(p)
    assert p == ['Changed',2,[3,5]]
    print('Test3 finished!')

test3()

def changeValue(var):
    var = 777
    return var

oriVar = 5

def test4():
    altVar = changeValue(oriVar)
    #assert altVar == oriVar #This will cause error. oriVar is immutable, altVar is a new local var refering to
    #a different value in memory
    print('altVar is ' + str(altVar))
    print('Test4 finished!')
    
test4()