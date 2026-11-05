class Solution(object):
    def findNumbers(self, nums):
       count=0
       for i in range(len(nums)):
        digits=len(str(nums[i]))
        if digits % 2==0:
            count+=1
       return count
        