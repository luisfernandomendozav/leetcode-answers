class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram = {}
        #1)- Lets take for example s = 'anagram', and t = 'margana'.

        #2)- This two words uses the same leter so t is an anagram of s.
        
        #3)- We first take care of one edge case, that is if the lengths are not equal
        # then those aren't anagrams.

        if len(s) != len(t):
            return False
        
        #3)- Lets form a hashmap with the letters of s, and the times that each letter repeat on the word
        # s = { a:3, n=1, g=1, r=1, m=1 }.

        for a in s:
            # If the element is not in the anagram we initialize this as 1
            if a not in anagram:
                anagram[a] = 1
            # If the element is in the anagram we add 1 to this key
            else:
                anagram[a] += 1

        #5)- Then lets compare this hash map with the t string.
        
        #6)- The first letter is 'm' so that means that we have to look into the
        # anagram hashmap to see if the letter is there.
        
        for b in t:
            # If the letter is not in the anagram that means t is not an anagram of s
            if b not in anagram:
                return False
            if b in anagram:
                # If the letter is in the anagram but with a value less than one, that means that
                # this letter repeats more times in the second string 't', so it's not an anagram.
                if anagram[b] < 1:
                    return False
                # We decrease by 1 if the letter repeats in the second string.
                else:
                    anagram[b] -= 1
        #7)- We return True if the 't' string pass all the above conditions
        return True