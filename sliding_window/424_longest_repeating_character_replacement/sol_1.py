class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1) - First we have to know that If we have a string like 'ABBCD'
        # the length of the string minus the number of times of the character
        # that most repeat in the string needs to be less or equal than k, that is because
        # we want to have to longest substring with the most characters repeated so
        # we do not want to change the character that repeat the most.

        # 2) - We initialize our result by 0 and our left pointer in 0 as well, we will be analyzing
        # each substring.

        # 3) - We make our tipical sliding window configuration, seting our left pointer yo 0, and
        # goinf trough all the right characters in the string.

        # 4) - We update our counter to keep track of all the characters that appear in the string.

        # 5) - If the length of the string (r - l + 1) minus the max of the values in count is greater
        # than k that means that we do not need to take account of that specific substring so we update
        # our left pointer.

        # 6) - then we update our result. 
        count = {}
        res = 0
        l=0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1    
            else: 
                count[s[r]] += 1
            while ((r-l+1) - max(count.values())) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
