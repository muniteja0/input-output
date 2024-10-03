'''
There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?

Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'

Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting

Sample Input:
30
40
20
25

Sample Output:
L1

'''



L1_capacity = int(input("Enter the seating capacity of L1: "))
L2_capacity = int(input("Enter the seating capacity of L2: "))
L3_capacity = int(input("Enter the seating capacity of L3: "))


num_students = int(input("Enter the number of students: "))


labs = [("L1", L1_capacity), ("L2", L2_capacity), ("L3", L3_capacity)]
labs = [lab for lab in labs if lab[1] >= num_students]
labs.sort(key=lambda x: abs(x[1] - num_students))


if labs:
    print(labs[0][0])
else:
    print("No lab can accommodate the 'n' number of students")
