import numpy as np

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed = np.array(list(allowed))
        count = 0

        for word in words:
            valid = True

            for ch in word:
                if ch not in allowed:
                    valid = False
                    break

            if valid:
                count += 1

        return count
        