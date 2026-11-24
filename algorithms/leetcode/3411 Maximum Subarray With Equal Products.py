class Solution(object):
    def maxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def prod(arr):
            product = arr[0]
            for i in range(1,len(arr)):
                product *= arr[i]
            return product
        def gcd(arr):
            numbers = 0
            a = arr[0]
            for i in range(1, len(arr)):
                b = arr[i]
                while b != 0:
                    a,b = b, a%b
            return a
        def lcm(arr):
            val = arr[0]
            for q in range(1,len(arr)):
                temp = [val, arr[q]]
                val = abs(prod(temp))/gcd(temp)
            return val
        maximum = 0
        for q in range(0, len(nums)):
            arr = [nums[q]]
            for j in range(q+1, len(nums)):
                arr.append(nums[j])
                if prod(arr) == (lcm(arr) * gcd(arr)):
                    if maximum < len(arr):
                        maximum = len(arr)
        return maximum