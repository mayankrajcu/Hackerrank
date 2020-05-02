""" Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

INPUT FORMAT:-
The first line contains an integer N.

OUTPUT FORMAT:-
Output the answer as explained in the task.

SAMPLE INPUT 0:-
3

SAMPLE OUTPUT 0:-
123 
"""
#SOLUTION:

def math(n):
    for i in range(1, n+1):
        print(i, end= '')

if __name__ == "__main__":
    n = int(input().strip())
    math(n)