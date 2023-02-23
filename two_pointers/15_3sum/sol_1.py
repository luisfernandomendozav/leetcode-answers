class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort()
            res = []
            for i,n in enumerate(nums):
                if i > 0 and n == nums[i-1]:
                    continue           
                l,r = i+1,len(nums)-1
                while l < r:
                    totalSum = n + nums[l] + nums[r]
                    if totalSum < 0:
                        l += 1
                    elif totalSum > 0:
                        r -= 1
                    if totalSum == 0:
                        res.append([n, nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l-1] and l < r:
                            l += 1
                    
            return res
