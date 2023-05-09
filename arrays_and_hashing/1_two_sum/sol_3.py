class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
