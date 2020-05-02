""" 
TASK:-
Read two integers and print two lines. The first line should contain integer division, a // b. 
The second line should contain float division, a / b.
You don't need to perform any rounding or formatting operations.

INPUT FORMAT:-
The first line contains the first integer, a. The second line contains the second integer, b.

OUTPUT FORMAT:-
Print the two lines as described above.

SAMPLE INPUT 0:-
4
3

SAMPLE OUTPUT 0:-
1
1.33333333333 
"""

def division_num(a,b):
    result = int(a//b)
    result1 = float(a/b)
    print('The integer division of and b is: ', result)
    print('The float devision of a and b is: ', result1)

if __name__ == "__main__":
    a = int(input().strip())
    b = int(input().strip())
    division_num(a,b)