'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.

Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training

Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting

Sample Input:
30
40
20
L3

Sample Output:
L1
'''

L1_capacity = int(input("Enter the seating capacity of L1: "))
L2_capacity = int(input("Enter the seating capacity of L2: "))
L3_capacity = int(input("Enter the seating capacity of L3: "))


allocated_lab = input("Enter the lab allocated for ACE training (L1, L2, or L3): ")


available_labs = []
if allocated_lab != "L1":
    available_labs.append(("L1", L1_capacity))
if allocated_lab != "L2":
    available_labs.append(("L2", L2_capacity))
if allocated_lab != "L3":
    available_labs.append(("L3", L3_capacity))


min_capacity = min(available_labs, key=lambda x: x[1])[0]


print(min_capacity)
