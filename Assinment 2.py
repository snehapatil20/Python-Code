#Question  1
s = '111100001111'
s=s.replace("1","a")
print(s)
s=s.replace("0","1")
print(s)
s=s.replace("a","0")
print(s)
"""
Output-
aaaa0000aaaa
aaaa1111aaaa
000011110000
"""
#Question 2
"""
rstrip - Trims characters from the right side of a string
lstrip- Trims characters from the left side of a string
"""
s1= "***My Name is Sneha***"
print(s1.rstrip("*"))
#Output- ***My Name is Sneha

s1= "***My Name is Sneha***"
print(s1.lstrip("*"))
#Output- My Name is Sneha***
#Question  3
#Homogeneous list is a list which is having a same type of data like following list is having same type of data as an Integer

s1=[1,2,3,4,5,5,6]

print(s1)
#Output -[1, 2, 3, 4, 5, 5, 6]

#Homogeneous list is a list which is having a different type of data like following list is having string , int, boolean


s1=["Sneha",2,True]

print(s1)
#Output -['Sneha', 2, True]

#Append

L1=[]

L1.append("Mango")
print(L1)
#Output - ['Mango']

L1.extend(["Banana","Apple",[1,2,3]])
print(L1)
#Output - ['Mango', 'Banana', 'Apple', [1, 2, 3]]

L1.clear()
print(L1)
#Output - []

