
# Given an array arr[] of positive integers and another integer target. Determine if there exist two distinct indices such that the sum of their elements is equal to the target.

# method 1 : Using two pointers: works with sorted array

def solve(nums,target):
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
print(solve(nums,target))

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
