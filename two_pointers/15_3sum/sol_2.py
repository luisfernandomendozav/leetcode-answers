class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []
            for i,n in enumerate(nums):
                l,r = i+1, len(nums)-1
                while l < r:
                    if n + nums[l] + nums[r] == 0 and [n,nums[l],nums[r]] not in res:
                        res.append([n,nums[l],nums[r]])
                        l += 1
                    elif n + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        r -= 1
            return res
