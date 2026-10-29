import numpy as np
class Solution(object):
    def getConcatenation(self, nums):
       nums=np.array(nums)
       return np.concatenate((nums,nums)).tolist()
           
