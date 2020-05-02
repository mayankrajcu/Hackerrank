"""
TASK:-
Given an integer, n, perform the following conditional actions:
-> If n is odd, print Weird
-> If n is even and in the inclusive range of 2 to 5, print Not Weird
-> If n is even and in the inclusive range of 6 to 20, print Weird
-> If n is even and greater than 20, print Not Weird

INPUT FORMAT:-
A single line containing a positive integer, n.

CONSTRAINTS: 1<=n<=100

OUTPUT FORMAT:-
Print Weird if the number is weird; otherwise, print Not Weird.

SAMPLE INPUT 0:-
3

SAMPLE OUTPUT 0:-
Weird

EXPLAINATION 0:-
n = 3
n is odd and odd numbers are weird, so we print Weird.

SAMPLE INPUT 1:-
24

SAMPLE OUTPUT 1:-
Not Weird

EXPLAINATION 1:-
n = 24
n > 20 and n is even, so it isn't weird. Thus, we print Not Weird. 
"""

#SOLUTION:-

def weird_not_weird(n):
    if n %2 != 0:
        print('weird')
    elif 2<= n%2==0 <= 5:
        print('Not Weird')
    elif 6<= n%2==0 <= 20:
        print('Weird')
    else:
        if n%2==0 > 20:
            print('Not Weird')


if __name__ == "__main__":
    n = int(input().strip())
    weird_not_weird(n)