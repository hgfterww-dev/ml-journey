class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            show = ""
            times = len(s)//k
            if len(s)%k >= 1:
                times += 1
            for i in range(times):
                result = 0
                newstring = ""
                newstring += s[(k*i):(k*(i+1))]
                for q in newstring:
                    result += int(q)
                show += str(result)
            s = str(show)
        return s