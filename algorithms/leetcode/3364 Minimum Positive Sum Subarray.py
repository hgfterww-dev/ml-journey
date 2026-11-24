class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        minSize = float("inf")
        for i in range(len(nums)):
            arr = []
            for q in range(i,len(nums)):
                arr.append(nums[q])
                if len(arr) >= l and len(arr) <= r:
                    if minSize > sum(arr) and sum(arr) > 0:
                        minSize = sum(arr)
        if minSize == float("inf"):
            return -1
        return minSize
        