class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1) - First Im have going to traverse the array

        # 2) - Then I'm going to store in a hash map the numbers that I have traverse.

        # 3) - Then I'm going to compare the number that I'm currently in with all the numbers that I have stored
        # in the hash map.
        nHash = {}
        for i,n in enumerate(nums):
            if i == 0:
                nHash[n] = i
                continue
            diff = target - n

            if diff in nHash:
                return [nHash[diff], i]
            nHash[n] = i
        return -1
        """
        Alternative solution

        numsMap = {}
        for i, n in enumerate(nums):
            numsMap[n] = i
        for i, n in enumerate(nums):
            search = target - n
            if search in numsMap and i != numsMap[search]:
                return [i, numsMap[search]]
        
        return -1

        """
