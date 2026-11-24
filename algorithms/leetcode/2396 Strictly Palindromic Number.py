class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def Base(n, b):
            listBase = []
            while n > 0:
                listBase.append(n%b)
                n //= b
            return listBase == listBase[::-1]
        for q in range(2, n-1):
            if not Base(n,q):
                return False
        return True