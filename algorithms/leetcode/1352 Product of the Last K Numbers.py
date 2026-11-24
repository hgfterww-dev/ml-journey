class ProductOfNumbers(object):

    def __init__(self):
        self.numbers = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if not num:
            self.numbers = [1]
        else:
            self.numbers.append(self.numbers[-1]*num)
        

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k >= len(self.numbers):
            return 0
        return self.numbers[-1] // self.numbers[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)