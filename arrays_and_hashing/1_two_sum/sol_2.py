class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, n in enumerate(nums):
            numsMap[n] = i
        print(numsMap)
        for i, n in enumerate(nums):
            search = target - n
            if search in numsMap and i != numsMap[search]:
                return [i, numsMap[search]]
        
        return -1