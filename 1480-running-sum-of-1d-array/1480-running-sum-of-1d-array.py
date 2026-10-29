import numpy as np
class Solution(object):
    def runningSum(self, nums):
        nums=np.array(nums)
        return np.cumsum(nums).tolist()
        