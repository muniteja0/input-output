'''
Write a program to create a list and display it.

Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list

Output format:
Output is an integer list

Sample Input
4
1
2
3
4

Output
1 2 3 4
'''


def create_list():
    
    n = int(input())
    user_list = [int(input()) for _ in range(n)]

    
    return user_list

def main():
    
    user_list = create_list()

    
    print(" ".join(map(str, user_list)))

if __name__ == "__main__":
    main()
