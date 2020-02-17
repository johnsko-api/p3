#the code for leet code to get it correct
"""
class Solution(object):
    def numberOfSteps (self, num):
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num-=1
            counter+=1
        return counter
"""
#recreating the code to work with user input
num = input("Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.")
def numberOfSteps(self,num):
        counter = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num-=1
            counter+=1
        return counter