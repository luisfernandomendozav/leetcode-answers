class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1) - Taking as an example th next pile array: 
        # [3, 6, 7, 11] the max number of bananas per hour will be
        # 11, since the last pile contains 11 bananas and that
        # is the maximum number of bananas in a pile, we just found the
        # max value of k.

        # 2) - We know have a range, because we start from 
        # 1 banana per hour since we can't start from zero
        # because that will mean that we are not eating any
        # bananas per hour, then at least we know that we the minimum
        # is between 1 and 11.

        # 3) - Next taking one "k" velocity we calculate of many hours will
        # take to eat all our bananas:
        # totalHours = math.ceil(piles[0]/k) + math.ceil(piles[1]/k) + ... 
        # ... + math.ceil(piles[n]/k)

        # 4) - If the total hours are less or equal than the time
        # that the zoo keepers are away then this velocity
        # "k" is a good candidate.

        # 5) - But since we are below or equal the total hours that
        # the zookepers are away, we try to find a k that is less
        # than the past k.

        # 6) - If k is greater than "h" then we need to lower our k.

        minK,maxK = 1, max(piles)
        k = maxK
        while minK <= maxK:
            currentK = (minK + maxK)//2
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile/currentK)
            if totalHours <= h:
                k = min(k,currentK)
                maxK = currentK - 1
            else:
                minK = currentK + 1
        return k

