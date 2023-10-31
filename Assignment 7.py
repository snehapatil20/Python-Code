 # 1-100 even numbers in reverse order
print(list(range(100,0,-2)))
 # 1-100 odd numbers in reverse order
print(list(range(99,0,-2)))
 # -10 to +10
print(list(range(-10,11)))
# -1 0 1
print(list(range(-1,2)))
"""
Output:
[100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
[99, 97, 95, 93, 91, 89, 87, 85, 83, 81, 79, 77, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]
[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[-1, 0, 1]
"""
# Q. What is frozenset
#-> It is similar to set , but it is immutable we can't add or delete the data from frozenset.
# Q. Difference between set and frozenset
# Main difference is the Frozenset is immutable , and set is mutable
# Set is not a hashable , frozenset is hashable.