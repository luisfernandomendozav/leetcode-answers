class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
            # 1) - The trick for this problem is to sort the array.

            # 2) - We are going to iterate through the array, and since this array 
            # is sorted we are going to use a two pointer solution.

            # 3) - We are going to look at items nums[i] nums[i+1] and 
            # nums[len(nums)-1].

            # 4) - If we move i to the right the nums get bigger.

            # 5) - If we move i to the left the nums get smaller.

            # 6) - So If n + nums[l] + nums[r] < 0, it means that we need to
            # go up in the sum we move the left pointer to the right.

            # 7) - If n + nums[l] + nums[r] > 0, it means that we need to
            # go down in the sum we move the right pointer to the left.

            # 8) - If n + nums[l] + nums[r] == 0, we have append the solution and
            # move the pointers.

            # 9) - The condition: 'if i > 0 and n == nums[i-1]:' is very important
            # because it restrain us from double counting the thriads, so we skip
            # repeated values for n.

            # 10) - The condition in the while loop it is also important because
            # it restrain us from double counting the thriads so we skip nums[l]
            # if nums[l] and nums[l-1] are equal.
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
