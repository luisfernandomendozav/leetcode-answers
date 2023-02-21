class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1) - The trick to this problem is to use a Set data structure.
        
        # 2) - First we need to identify what number is the first number of a sequence, and that is done
        # by checking if the current number has a left neighbor, i.e. if the current number minus one doesn't exists
        # in the set.

        # 3) - Once we identify if a number is the first number of a sequence, we start counting how many
        # consecutive numbers starting from the root of a sequence exists in the set, we do this using a while loop
        # we first check if the number n + 0 is in the sequence this will always return True since n is part of the original
        # array, that being the case the length variable gets incremented by one.

        # 4) - Then we check if the number n + 1 is in the sequence if it is we increment the length variable by one
        # and so on.

        # 5) - After the while loop we update the longest variable, and when we reach the end of the for loop we
        # return this variable.

        numSet = set(nums)
        longest = 0
        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest