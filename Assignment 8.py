# Assignment: use sorted over list,list of string,work on key,reverse
l1 = ["Sneha","OM","Kanha","Roshani","Shubham"]
print(sorted(l1,key = len))
print(sorted(l1))
print(sorted(l1,reverse=True,key = len))
#Output:

"""
['OM', 'Sneha', 'Kanha', 'Roshani', 'Shubham']
['Kanha', 'OM', 'Roshani', 'Shubham', 'Sneha']
['Roshani', 'Shubham', 'Sneha', 'Kanha', 'OM']


"""

l1 = ("Sneha","OM","Kanha","Roshani","Shubham")
print(sorted(l1,key = len))
print(sorted(l1))
print(sorted(l1,reverse=True,key = len))

"""
['OM', 'Sneha', 'Kanha', 'Roshani', 'Shubham']
['Kanha', 'OM', 'Roshani', 'Shubham', 'Sneha']
['Roshani', 'Shubham', 'Sneha', 'Kanha', 'OM']


"""
# Assignment: sort vs sorted
"""
sort()  method directly do changes in the existing list that is inplace 
sorted() method creates new list it does not do the changes in the list.
"""

# Q. Take a list/set/tuple/dict from user asn an input
l1 =eval(input("Enter List : "))
print(l1)
l2 =eval(input("Enter tuple : "))
print(l2)

l3 =eval(input("Enter dictionary : "))
print(l3)
#Outout :
"""
Enter List : [1,2,3]
[1, 2, 3]
Enter tuple : (2,3,4)
(2, 3, 4)
Enter dictionary : {1:"Sneha",2:"Nikita"}
{1: 'Sneha', 2: 'Nikita'}
"""

# Assignmnt: Apply reverse on list, list of string
l3=[3,2,7,9,4]
print(list(reversed(l3)))
#Output: [4, 9, 7, 2, 3]
l3=["Sneha","Sonu","Shubham"]
print(list(reversed(l3)))
#Output: ['Shubham', 'Sonu', 'Sneha']
