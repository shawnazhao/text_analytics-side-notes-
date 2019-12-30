#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:42:25 2019

@author: shawnaaaaaa
"""

# lamba functions are single line and short

add5=lambda x:x+5
print(add5(7))


square=lambda x:x*x
print(square(8))

# sorting a list of tuples using lambda
# sort by the alphabet here
list1=[(23,'s'),(34,'a'),(34,"c")]
list1.sort(key=lambda x:x[1])

print(list1)

# can also do a list of dictionary

list2=[{'make':'ford','model':'Focus','year':2013},{'make':'Tesla','model':'X','year':1999}]
list2.sort(key=lambda x: x['year'])
print(list2)

# filtering a list of integers using lambda

list1=[1,2,3,4,5,6]

#only keep the even number
list2=list(filter(lambda x: x%2==0,list1))

odds=lambda x: x%2==1
list3=list(filter(odds,list1))
print(list3)


#map function applies the lambda to every element in the list
list1=[1,2,3,4,5,6]
list2=list(map(lambda x: x**2, list1))
print(list2)


#lambda conditionals
# lambda args: a if boolean_expression else b
start_with_j=lambda x: True if x.startswith('J') else False
print(start_with_j('Jess'))


## get the word before

wordb4= lambda s,w,: s.split()[s.split().index(w)-1] if w in s else None
sentence='four score and seven years ago'
print(wordb4(sentence,'seven'))




 #lambdas on DataTime objects, you sometimes want to get just the year,month date time for comparison
 
 
import datetime
now=datetime.datetime.now()
print(now)


year=lambda x: x.year
print(year(now))

# another use of lambda

def do_something(f,val):
    return f(val)
func=lambda x: x**3
print(do_something(func,5))



#take away the negative sign
is_num=lambda r: isnum(r[1:]) if r[0]=='-' else isnum(r)
print(is_num('23.34'))

to_num= lambda s: float(s) if is_num(s) else -1
print(to_num('30y'))
print(to_num('-23.45'))



