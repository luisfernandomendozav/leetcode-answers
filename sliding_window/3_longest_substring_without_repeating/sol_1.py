class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1) - We make our configuration for a sliding window.

        # 2) - We are going to keep track in a set wich of the letter repeat, and If
        # the letters repeat we are goingi to eliminate the left most character and if not
        # we are goingi to add the right most characters.

        # 3) - We are updating our max to be the length of the set or our current res.
        
        count = set([])
        res = 0 
        l = 0 
        for r in range(len(s)):
            while s[r] in count:
                count.remove(s[l])
                l+=1
            count.add(s[r])
            res = max(res, len(count))
        return res