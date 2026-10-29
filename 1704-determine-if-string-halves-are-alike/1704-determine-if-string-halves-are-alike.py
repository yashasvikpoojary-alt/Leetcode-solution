import numpy as np

class Solution(object):
    def halvesAreAlike(self, s):
        s = np.array(list(s))
        vowels = "aeiouAEIOU"
        n = len(s) // 2
        a = 0
        b = 0

        for i in range(n):
            if s[i] in vowels:
                a += 1

        for i in range(n, len(s)):
            if s[i] in vowels:
                b += 1

        return a == b
        