class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1) - We use a left pointer and a right pointer for binary search

        # 2) - The tricky part is to unserstand how to find the middle point,
        # first we need to find the length of the segment and that always will be
        # (r - l), then we calculate thehalf of that segment (r - l) // 2, then
        # we need to translate "l" times to the left because we are using a
        # coordinate system.

        # 3) - If nums[m] are less than the target that means the target is 
        # in the second half of the interval, so we move the left pointer
        # to the right of "m" i.e "m+1".

        # 4) - If nums[m] is greater than the target that means the target is
        # in the first half of the interval , so we move the right pointer to 
        # the left of "m" i.e "m-1".

        # 5) - If none of those conditions are true we return "m".
        
        l,r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1
