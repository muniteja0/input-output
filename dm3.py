'''
The newly appointed Vice-Chancellor of Anna University wanted to create an automated grading system for the students to check their grade. When a student enters a mark, the grading system displays the corresponding grade.

Write a program to solve the given problem.

  Marks scored  

  Grade

100

S

90 - 99

A

80 - 89

B

70 - 79

C

60 - 69

D

50 - 59

E

<50

F

Input format:

The input consists of one integer which corresponds to the marks scored by the student


Output format:

If a student marks greater than 100, print "Invalid Input". Otherwise, print the grade.

Sample Input:
78

Sample Output:C
'''


marks = int(input("Enter your marks: "))


if marks > 100:
    print("Invalid Input")
else:
    
    if marks >= 90:
        print("A")
    elif marks >= 80:
        print("B")
    elif marks >= 70:
        print("C")
    elif marks >= 60:
        print("D")
    elif marks >= 50:
        print("E")
    else:
        print("F")
