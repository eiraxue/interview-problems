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
# find if the list has the target number, with recursion
def checkIfExist(inputList, low, high, x):
    if low<=high:
        mid = low + (high-low)/2
        if x<inputList[mid]:
            return checkIfExist(inputList, low, mid-1,x)
        elif x>inputList[mid]:
            return checkIfExist(inputList, mid, high,x)
        else:
            return mid
    return -1

testList = [-9, -3, 1, 3, 4, 8]
print checkIfExist(testList, 0, len(testList),3)  

#%%
 def checkIfExist(inputList, x):   
    N=len(inputList)
    if N>=1:
        if x < inputList[N/2]:
            return checkIfExist(inputList[:N/2-1], x)
        elif x > inputList[N/2]:
            return checkIfExist(inputList[N/2:], x)
        else:
            return N/2
    return -1

testList = [-9, -3, 1, 3, 4, 8]
print checkIfExist(testList, 3)  


#%%
# find if the list has the target number, plain implementation
import timeit

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

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped           

            
testList = [-9, -3, 1, 3, 4, 8]
print checkIfExist(testList, 7)  
print "function took %0.3f s" % timeit.timeit(wrapper(checkIfExist,testList, 7)) 

#%% compute x^N
import timeit
import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
    
@timing 
def computeXN(x,N):
    if N==0:
        return 1
    elif N==1:
        return x
    else :
        if N%2==0:
            return computeXN(x,N/2)*computeXN(x,N/2)
        else:
            return computeXN(x,N/2)*computeXN(x,N/2+1)
 
@timing       
def computeXN_efficient(x,N):
    if N==0:
        return 1
    elif N==1:
        return x
    else :
        if N%2==0:
            return computeXN_efficient(x*x,N/2)
        else:
            return computeXN_efficient(x*x,N/2)*x
            

test=2
N=20
print computeXN(test, N)
print computeXN_efficient(test, N)
