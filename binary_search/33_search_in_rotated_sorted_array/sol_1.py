class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1) - Since the problem is telling us that we need to write
        # and algorithm in O(log n) we can imagin that we need to use
        # binary search.

        # 2) - We know that we have a rotated sorted array so we can
        # divide this problem into two sub problem, we have two sub
        # arrays: [4,5,6,7,  0,1,2] all the numbers in the first sub array
        # are greater than all the numbers in the second sub array.

        # 3) - First we need to figure out on what sub array we are in, we
        # calculate the middle point "m", if nums[m] >= nums[l] that means we
        # are in a sorted array from l to m,and since nums[l] will always be
        # part of the first sub array, we know that nums[m] belongs to the
        # first sub array, so from index "l" to "m" we are in the first subarray

        # 4) - So if we are in the first sub array and nums[m] < target, we know
        # that the answer can only be to the right of "m" because everything that
        # is to the left of "m" is less than nums[m].

        # 5) - As well if target is less than nums[l], then that means that
        # the answer can only be on the second sub array, so thats why we move
        # the elft pointer to m + 1, because in the first case we answer can only
        # be to the right, and in the second case the answer can only be in the
        # second subarray that happens to be also to the right.

        # 6) Is we are in the second sub array, and nums[m] > target, that means 
        # that the answer can only be to the left and also if the target is
        # greater than nums[r] the answer can only be in the first sub array
        # that happens to be also tot he right, thats why we move the right
        # pointer.


        l,r = 0, len(nums)-1

        while l <= r:
            m = l + ((r-l)//2)
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m -1
            else:
                if nums[m] > target or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1