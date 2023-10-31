# Assignment
# Assignment: Solve any 3 example with inclusion of selective statements inside for loop
list1 =[1,2,5,5,7,55,35,67,89,10,25,75]
list2 =[]
for i in list1:
    if i%5==0:
        list2.append(i)
print("Number divided by 5 -: ", list2)

"""
Output -: 
Number divided by 5 -:  [5, 5, 55, 35, 10, 25, 75]
"""

list1 = [1,2,3,4,5,6,7,8,9,1,34,45,67,45,78,89,90]
l1=[]
l2=[]
for i in list1:
    if i%2==0:
        l1.append(i)
    elif i%2!=0:
        l2.append(i)

print("Positive Numbers -: ",l1)
print("Negative Numbers -: ", l2)
"""
Output :
Positive Numbers -:  [2, 4, 6, 8, 34, 78, 90]
Negative Numbers -:  [1, 3, 5, 7, 9, 1, 45, 67, 45, 89]

"""
list3 = ["Sneha","om","%","Shubham","89"]
special = ["!","@","#","$","%","^","&","*"]
for i in list3:
    if i.isdigit():
        list3.remove(i)
    elif i in special:
        list3.remove(i)
print(list3)

"""
Output :
['Sneha', 'om', 'Shubham']
"""
"""
Assinment -: 

*****
****
***
**
*
"""

for i in range(5,0,-1):
    print(i*'*')

"""
*****
***
*
"""
for i in range(5,0,-1):
    print(i*"*")
""" 
Assignment:

AAAA
BBB
CC
D

"""
n=4
no = 65
for i in range(1,n+1):
    for j in range(n,i-1,-1):
         print(chr(ord('A')-1+i),end="")
    no=no+1
    print("")
"""




A
AB
ABC
ABCD
ABCDE
"""

for i in range(1,6):
    n = 65
    for j in range (1,i+1):
        print(chr(n),end="")
        n=n+1
    print()

"""
ABCDE
ABCD
ABC
AB
A
"""

for i in range(0,5):
    n = 65
    for j in range(5,i,-1):
        print(chr(n), end="")
        n=n+1
    print()


