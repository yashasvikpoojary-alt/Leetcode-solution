import numpy as np
class Solution(object):
    def toLowerCase(self, s):
        s=np.array(list(s))
        ans=""
        for i in range(len(s)):
            ans+=s[i].lower()
        return ans