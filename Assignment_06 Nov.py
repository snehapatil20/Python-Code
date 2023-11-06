# Assignment: to check 4 different types of arguments example in lambda and test it
s1 = lambda a , b: a+b
print(s1(9,2)) #--------------Positional Arguments
#Output : 11

s2 = lambda a=9, b=8 , c=7 : a+b+c
print(s2(23,12,45))
#Output : 80

s3  = lambda a , b , c: a+b+c
print(s2(b=3, a=9, c=7))
#Output : 19


#Variable Length Arguments
s4 = lambda *n : [i*i for i in n]
print(s4(1,2,3,5,8))
#Output : [1, 4, 9, 25, 64]

def s1 (*n):
    print([i*i for i in n])
s1(1,2,3)
#output : [1, 4, 9]

s3 = lambda a: "Even" if a%2==0 else "Odd"
print(s3(22))
print(s3(7))

"""
Even
Odd
"""
s3 = lambda a: "Positive" if a>0 else "Negative"
print(s3(22))
print(s3(-7))
"""
Positive
Negative
"""

s4 = lambda a: "Buy Vehicle" if a>100000 else "Don't Buy Vehicle"
print(s4(300000))
print(s4(10000))
"""
Buy Vehicle
Don't Buy Vehicle
"""
#Map Function
n1 = [10,20,30,40]
square = lambda n2 : n2 * n2
print(list(map(square , n1)))

#Output : [100, 400, 900, 1600]

n2 = ["Sneha", "Shubham", "Nikita"]
UpperCase = lambda n2 : n2.upper()
print(list(map(UpperCase,n2)))
#Output : ['SNEHA', 'SHUBHAM', 'NIKITA']

n2 = ["Sneha", "Shubham", "Nikita"]
LengthString = lambda n2 : len(n2)
print(list(map(LengthString, n2)))

#Output : [5, 7, 6]


#Filter Function

n1 = [1, 90,45,7,45,-7,5,7,8,-9]
n3 = lambda n4 : n4 > 0
print(list(filter(n3,n1)))
#Output : [1, 90, 45, 7, 45, 5, 7, 8]

n1 = ['1', '9.7','45','7',"Sneha","ABC",'5','7','8','-9']
n2 = lambda n3 : n3.isalpha()
print(list(filter(n2, n1)))
#Output : ['Sneha', 'ABC']

from functools import reduce
nums = [2.45,67,89,78]
n1 = lambda a, b : a-b
print(reduce(n1, nums))
#Output : -231.55

nums = [2.45,67,89,78]
n1 = lambda a, b : max(a,b)
print(reduce(n1, nums))
#Output : 89

nums = [2.45,67,89,78]
n1 = lambda a, b : min(a,b)
print(reduce(n1, nums))
#Output : 2.45