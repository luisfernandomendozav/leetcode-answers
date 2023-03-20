class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1) - First we have to know that this is a two pointer solution,
        # we will start by defining the left pointer and the right pointer.

        # 2) - The left pointer is going to be the the first indes and the right pointer is going to e
        # the second index.

        # 3) - If the left pointer is higher than the right pointer we update our pointers,
        # we make the left pointer equals to the right pointer and the right pointer one
        # more thant the left pointer.
        
        l,r = 0,1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
            tmp = prices[r] - prices[l]
            profit = max(profit, tmp)
            r += 1
        return profit if profit >= 0 else 0
