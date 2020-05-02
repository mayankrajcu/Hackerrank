""" 
TASK:-
Read an integer N. For all non-negative integers i < N, print i^2. See the sample for details.

INPUT FORMAT:-
The first and only line contains the integer, .

CONSTRAINTS:-
1 <= N <= 20

OUTPUT FORMAT:-
Print N lines, one corresponding to each i.

SAMPLE INPUT 0:-
5

SAMPLE OUTPUT 0:-
0
1
4
9
16
"""
# SOLUTIONS:-

def loopy(n):
    for i in range(n):
        result = i**2
        print(result)

if __name__ == "__main__":
    n = int(input().strip())
    loopy(n)