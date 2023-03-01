class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1) - If the array is rotated 0 times then the first number will be the minimum

        # 2) - The minimum will be at the pivot.

        # 3) - We are going to define a l,r = 0, len(nums).

        # 4) - We are going to calculate the middle point m = l + (r-l)//2

        # 5) - We store the minmum as nums[m]

        # 6) - If nums[m] > nums[l], suppose we have the next array:
        # [l-4, 5, (6), 0, 1, 2, 3-r  ] then we are in the right array so that means that
        # we need to go to the left sub array, so we move the left pointer l = m + 1.

        # 7) - If nums[m] < nums[l], that means that m is in the left sub array.

        # 8) - Then we move the right pointer to r = m - 1.

        l,r = 0, len(nums)-1
        minN = nums[l]
        while l <=r:
            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break
            m = l + ((r-l)//2)
            minN = min(minN, nums[m])
            if nums[m] >= nums[l]: # That means we are in the right sub array
                l = m+1
            else:
                r = m - 1
        return minN



