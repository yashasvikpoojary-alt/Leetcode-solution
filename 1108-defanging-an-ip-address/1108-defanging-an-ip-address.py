import numpy as np
class Solution(object):
    def defangIPaddr(self, address):
       address=np.array(list(address))
       ans=""
       for i in range(len(address)):
        if address[i] == "." :
            ans +="[.]"
        else:
            ans +=address[i]
       return ans
    
