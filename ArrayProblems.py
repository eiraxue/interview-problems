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

#%%
# find if the list has the target number
def checkIfExist(inputList, x):
    N=len(inputList)
    if N==1:
        if x!= inputList[0]:
            return false
        else:
            return true
    if x < inputList[N/2]:
        checkIfExist(inputList[:N/2-1], x)
    elif x > inputList[N/2]:
        checkIfExist(inputList[N/2+1:], x)
    else:
        return true
    
testList = [-9, -3, 1, 3, 4, 8]
print checkIfExist(testList, -9)  


#%%
# find if the list has the target number, plain implementation
def checkIfExist(inputList, x):
    low = 0
    high = len(inputList)-1
    while(low <= high):
        mid = (low+high)/2
        if x<inputList[mid]:
            high = mid-1
        elif x>inputList[mid]:
            low = mid+1
        else:
            return mid
    return -1
            
testList = [-9, -3, 1, 3, 4, 8]
print checkIfExist(testList, 7)  
