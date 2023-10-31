"""
Questions
- break vs continue
- similarity btwn break and continue
- what is pass/use of pass
"""
"""
- break vs continue

Break statement stops the entire process of the loop. Continue statement only stops the current iteration of the loop. 
Break also terminates the remaining iterations. Continue doesn't terminate the next iterations;

- similarity btwn break and continue
Both are used to terminate the iterations.

- what is pass/use of pass

Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
to avoid error's we can use pass keyword to in empty code.
"""

list1 = [1,4,6,9,8,7,67,98,90,45]
print([i**2 for i in list1])
#[1, 16, 36, 81, 64, 49, 4489, 9604, 8100, 2025]

print(["Even" if i%2==0  else "odd" for i in list1])
#['odd', 'Even', 'Even', 'odd', 'Even', 'odd', 'odd', 'Even', 'Even', 'odd']

names = ['sneha','shubham','nikita']

print([n.upper() for n in names])
#['SNEHA', 'SHUBHAM', 'NIKITA']
e = (23,13,4,56,10)
print([i*100 for i in e])
#[2300, 1300, 400, 5600, 1000]

print([[i] for i in e])
#[[23], [13], [4], [56], [10]]

print([[i,float(i)] for i in e])
#[[23, 23.0], [13, 13.0], [4, 4.0], [56, 56.0], [10, 10.0]]

print([[i,i**2] for i in e])
#[[23, 529], [13, 169], [4, 16], [56, 3136], [10, 100]]
n1 = [1,4,-5,-7,-9,8]
print([i for i in n1 if i>0])
#[1, 4, 8]
print([i for i in n1 if i<0])
#[-5, -7, -9]
print([abs(i) for i in n1 if i<0])
#[5, 7, 9]
n2 = [0,1,1,0,1,1,0]
print(["Male" if i==0 else "Female" for i in n2])
#['Male', 'Female', 'Female', 'Male', 'Female', 'Female', 'Male']
covid = [98,99,87,86,81,77,99]
print(['Covid+' if temp>90 else 'Covid-' for temp in covid])
#['Covid+', 'Covid+', 'Covid-', 'Covid-', 'Covid-', 'Covid-', 'Covid+']

