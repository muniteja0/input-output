'''
Write a Python Program to find the smallest number in a list

Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.

Sample Input:
5
1
2
3
6
5

Sample Output:
1
'''

def find_smallest_number():
    
    n = int(input())

    
    smallest_number = min(int(input()) for _ in range(n))

    
    return smallest_number

def main():
    
    smallest_number = find_smallest_number()

    
    print("Smallest Number:", smallest_number)

if __name__ == "__main__":
    main()
