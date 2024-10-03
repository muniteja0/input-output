'''

Write a Python Program to find the largest number in a list

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
6

'''

def find_largest_number():
    
    n = int(input())

    
    largest_number = max(int(input()) for _ in range(n))

    
    return largest_number

def main():
    
    largest_number = find_largest_number()

    
    print("Largest Number:", largest_number)

if __name__ == "__main__":
    main()
