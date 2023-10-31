
# Assignment:
#- print 10-0 numbers
num = 10
while num>-1:
    print(num)
    num = num -1

"""
Output : 
10
9
8
7
6
5
4
3
2
1
0
"""
#- print -5 to 5 numbers
num = -5
while num<6:
    print(num)
    num = num + 1

"""
Output :
-5
-4
-3
-2
-1
0
1
2
3
4
5

"""

#- print 1-20 even numbers
num = 1
while num<=20:
    if num%2==0:
        print(num)
    num = num +1

"""
Output - : 
2
4
6
8
10
12
14
16
18
20
"""
#- print 1-20 odd numbers
num = 1
while num<=20:
    if num%2!=0:
        print(num)
    num = num +1
"""
Output : 
3
5
7
9
11
13
15
17
19

"""
#- check number is even or odd
check = "yes"

while True:
    check = input("Do you want to check number?")
    if check=="no":
        break
    num = int(input("Enter Number : "))
    if num%2==0:
        print(num , "is even")
    else:
        print(num, "is odd")

"""
Output -: 
Do you want to check number?yes
Enter Number : 2
2 is even
Do you want to check number?yes
Enter Number : 9
9 is odd
Do you want to check number?no

"""




#- check number is +ve or -ve

while True:
    check = input("Do you want to check number?")
    if check=="no":
        break
    num = int(input("Enter Number : "))
    if num>0:
        print(num , "is positive")
    elif num<0:
        print(num, "is negative")
    else:
        print("It is a 0")

"""
Output : 
Do you want to check number?yes
Enter Number : 9
9 is positive
Do you want to check number?yes
Enter Number : -6
-6 is negative
Do you want to check number?yes
Enter Number : 0
It is a 0
Do you want to check number?no

"""