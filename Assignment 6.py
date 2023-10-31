# Assignment: pop vs popitem
#1) Pop - This method is use to remove an element from dictionary using key, using this method we can handle
#exception handling i.e instead for Key Value error we can return other value when key is not present in the dictionary.
a={"Maths":20, "Science": 23, "English":15,"Geography": 20}
a.pop("Maths")
print(a)
#Output : {'Science': 23, 'English': 15, 'Geography': 20}
print(a.pop("Maths", "Key is not present"))

#output: Key is not present

#2) Popitem : Popitem is use remove the key , value pair , it will remove and returned the
# key, value pair.
#It remove's last key, value pair from the dictionary.
a={1:23,2:34,3:45,5:56,6:67}
print(a.popitem())
#Output : (6, 67)

# Create a dict with 5 key value pairs and apply all the methods
a={1:20,2:23,3:24,4:6,7:24,8:25,5:23}
print(a.keys())
print(a.values())
print(a.items())
print(a.pop(1))
print(a.popitem())
print(a.fromkeys([11,23]))
print(a.get(2))
print(a.update({9:5}))
print(a.setdefault(1,'NA'))
b=[12,56]
print(dict.fromkeys(b,4))
print(a)
print(a.clear())
#Output:
"""
dict_keys([1, 2, 3, 4, 7, 8, 5])
dict_values([20, 23, 24, 6, 24, 25, 23])
dict_items([(1, 20), (2, 23), (3, 24), (4, 6), (7, 24), (8, 25), (5, 23)])
20
(5, 23)
{11: None, 23: None}
23
None
NA
{12: 4, 56: 4}
{2: 23, 3: 24, 4: 6, 7: 24, 8: 25, 9: 5, 1: 'NA'}
None
{1: 5, 2: 6, 3: 7}

"""
# we have 2 list x = [1,2,3] y = [5,6,7] ,Create a dict {1:5,2:6,3:7}
# where a x value should act as a key and y value should act as a value of dict
x = [1,2,3]
y = [5,6,7]
d = {}
d =dict(zip(x,y))
print(d)
#Output : {1: 5, 2: 6, 3: 7}

