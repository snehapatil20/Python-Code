
#Assignment
# What is Indentation
"""
Indentation is nothing but the whitespaces given at the right side of the code ,
it tells python interpereter the scope of the block i.e means the start and end of the code block.
"""
#Solve 3 Examples of each topic
#1)If

#Example - If student scores 35% or more  35% marks in the exam then he will pass.
marks = int(input("Enter marks in % - : "))
if marks>=35:
    print("Pass")

#Output -:

"""
When input is 34 - Nothing will print
if input is 78 output will be - Pass
"""
# 2) Example - If mango is present in bascket then no need to purchase it, if present the output will be please purchase mango.
list1 = ["Banana", "Pine Apple", "Apple"]
if "mango" not in list1:
    print("Please , Purchase mango")
 # 3)Example - If its a Sunday then it will be a holiday.

day = input("Enter a day : ")
if day =="Sunday":
     print("It's a holiday....")

"""
Output -: 
if day is monday then it will not print anything 
if day is Sunday then it will print , It's a holiday.....

"""
#1)If - else
#1) Example - if student scores more than equal to 35 % then then he will be pass otherwise fail.
marks = int(input("Enter Marks -: "))
if marks >=35:
    print("Pass")
else:
    print("Fail")
#Output :
"""
if input is 35 , it will print Pass
if input is 67 , it will print Pass
if input is 23 , it will print Fail
"""
# 2) Example - If mango is present in bascket then it will print no need to purchase it, if present the output will be please purchase mango.
list1=["banana", "mango","pine apple"]
if "mango" in list1:
    print("no need to  purchase mango.")

else:
    print("Need to purchase mango")

#output -:
"""
if mango is there is the list the it will print -: no need to  purchase mango.
else it will print - : Need to purchase mango
"""
# 3)Example - If its a Sunday then it will be a holiday , otherwise it will print it's a working day.
day = input("Enter the day -: ")
if day == "Sunday":
    print("It's a holiday")
else:
    print("It's a working day")

#If - elif - else

# if student scores 35 or more than 35  and less than less than 60 then  pass, if more than 60 and less than 75 then first class , if more than 75 then Distinction.
marks = int(input("Enter marks - : "))
if marks >= 35 and marks < 60:
    print("Pass")
elif marks>60 and marks<75:
    print("First Class")
elif marks > 75:
    print("Distinction")
else:
    print("Fail")

"""
Output : 
Enter marks - : 34
Fail
Enter marks - : 65
First Class
Enter marks - : 78
Distinction
Enter marks - : 55
Pass
"""
# 2) Example - check number is positive or negative.
j = int(input("Enter Number : "))
if j>0:
    print("Number is positive.")
elif j<0:
    print("Number is negative")
else:
    print("Number is 0")

"""
Output : 
Enter Number : 6
Number is positive.
Enter Number : -6
Number is negative.
Enter Number : 0
Number is 0.
"""
#Example - Traffic Signal

colour = input("Enter Colour : ")
if colour=="red":
    print("Stop")
elif colour=="green":
    print("Go")
elif colour("Yellow"):
    print("Go slow")
"""
Output : 
Enter Colour : red
Stop
Enter Colour : green
Go
Enter Colour : Yellow
Go Slow
"""

