# -*- coding: utf-8 -*-
"""
Solutions of Array problems in software engineering 

2016/09/28
"""

#%%
# return all the pairs with sum as target value
def findTwoNumbersWithSum(inputList, target):
    i=0
    j=len(inputList)-1
    while(i<j):
        sum=inputList[i]+inputList[j]
        if sum<target:
            i+=1
        elif sum>target:
            j-=1
        else:
            print "Find one pair %d, %d" % (inputList[i], inputList[j])
            i+=1
            j-=1  

# main caller starts here
testList = [1, 2,3, 4, 7,11,12,15]
findTwoNumbersWithSum(testList, 15)

#%%
# find the subsequence with max sum
def findMaxSumSequence(inputList):
    maxSum=inputList[0]
    sum=0
    for ele in inputList:
        sum+=ele
        if sum > maxSum: 
            maxSum=sum
        elif sum < 0:
            sum=0
    print "Max Sum of Subsequence: %d" % maxSum
    
testList = [-4, 2, 3, 0, -1, 10, 2, -3]
findMaxSumSequence(testList)