# link - https://practice.geeksforgeeks.org/problems/addition-under-modulo/1/?track=ppc-mathematics&batchId=221

# You are given two numbers a and b. You need to find the sum of a and b under modulo M.
# Note: Take M as 10^9+7

# Input:
# 2
# 9223372036854775807 9223372036854775807
# 1000000007 1000000007

# Output:
# 582344006
# 0

#User function Template for python3
def sumUnderModulo(a,b):
    '''
    :param a: given value of a
    :param b: given value of b
    :return: Integer , sum under modulo
    '''
    M = 1000000007
    # code here
    return (a+b)%M

#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a,b = map(int,input().strip().split())
        print(sumUnderModulo(a,b))
