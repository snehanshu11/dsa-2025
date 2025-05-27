
# Given an array arr[] of positive integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

# method 1 : Using two pointers: works with sorted array

def solve_two_pointer(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        if nums[left]+nums[right]==target:
            return [left,right]
        elif nums[left]+nums[right]>target:
            right-=1
        elif nums[left]+nums[right]<target:
            left+=1
    return [-1,-1]

nums=[1, 2, 3, 4, 5, 6]
target=11
print(solve_two_pointer(nums,target))

def solve_naive(nums,target):
    l=len(nums)
    for i in range(0,l-1):
        for j in range(i+1,l):
            if nums[i]+nums[j]==target:
                return [i,j]
    return [-1,-1]
        
nums=[1, 2, 3, 4, 5, 6]
target=10
print(solve_naive(nums,target))

def solve_hashmap(nums,target):
    hm={}
    for i in range(len(nums)):
        print(hm)
        complement = target - nums[i]
        if nums[i] not in hm:
            hm[complement]=i
        else:
            return [hm[nums[i]],i]
    return [-1,-1]
        
nums=[1, 2, 3, 4, 5, 6]
target=11
print(solve_hashmap(nums,target))

def solve_backtrack(index,total,target,lst):
    
    if total==target:
        if len(lst)==2:
            res.append(lst.copy())
            return
        
    if index>=len(nums):
        return

    lst.append(index)
    total+=nums[index]
    solve_backtrack(index+1,total,target,lst)
    lst.pop()
    total-=nums[index]
    solve_backtrack(index+1,total,target,lst)
    
        
res=[]        
nums=[1, 2, 3, 4, 5, 6]
target=10
lst=[]
solve_backtrack(0,0,target,lst)
print(res)
