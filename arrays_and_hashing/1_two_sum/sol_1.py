class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i in range (len(nums)):
            kSearch = target - nums[i]
            if(kSearch in store):
                return [i, store[kSearch]]
            store[nums[i]] = i
        return -1