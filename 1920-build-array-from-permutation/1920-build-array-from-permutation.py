import numpy as np
class Solution(object):
    def buildArray(self, nums):
        nums=np.array(nums)
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans    
        