#Assignment 1
#Difference between add and update
#1)Add is used to add the single elements to the set as follows,
# add method can't accept multiple elements.
a=set()
a.add(6)
print(a)
#output -: {6}
#2) Update is use to add the multiple elements to the set as follows ,
# update method can't accept single element it needs iterable elements only
b=set()
b.update([1,2,3,4,5])
print(b)
#output : {1, 2, 3, 4, 5}

#Assingment 2
#What is the difference between pop, remove and discard?
#1)Pop - This method removes random element from the set .
a={2,3,4,5,'Good', 'Bad'}
a.pop()
print(a)
#Output -: {2, 3, 4, 5, 'Bad'}

#2)Remove - This method is use to remove particular element from the set as follows.
#If element is not found in the set it will through an error.
a={4,3,7,5,9,0}
a.remove(3)
print(a)
#Output -: {0, 4, 5, 7, 9}

#3)Discard - This method as well use to remove a particular element from the set.
#If element is not found in the set it will not through an error.
a={2,23,5,56,6,7}
a.discard(5)
print(a)
#Output -: {2, 23, 6, 7, 56}


# Assignment 3 : Can we perform packing and unpacking over set
#Yes , we can perform packing and inpacking over set as follows
k ={2,56,4,7,8}
print(k)
a,b,c,d,e = k
print(a)
print(b)
print(c)
print(d)
print(e)
"""output - : {2, 4, 7, 8, 56}
2
4
7
8
56
"""
# Assinment - : s1 = {4,5,6,7} s2 = {4,6,8,9} perform all operations of set
s1 = {4,5,6,7}
s2 = {4,6,8,9}
print(s1.union(s2))
#Output -: {4, 5, 6, 7, 8, 9}
print(s1.intersection(s2))
#Output -: {4, 6}
print(s1.difference(s2))
#Output -: {5, 7}
print(s2.difference(s1))
#Output -: {8, 9}
print(s2.symmetric_difference(s1))
#Output -: {5, 7, 8, 9}
s3={5,8,9,0,6}
s4={2,4,5,6,7}
s1.intersection_update(s2)
print(s1)
#Output -: {4, 6}
s3.difference_update(s2)
print(s3)
#Output -:{0, 5}
s4.symmetric_difference_update(s2)
print(s4)
#output -: {2, 5, 7, 8, 9}


