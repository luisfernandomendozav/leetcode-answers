class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) - First we are going to create a new string with no special characters and no spaces

        # 2) - Then we are going to use that new string and to a two pointer solution, intializing the
        # left pointer to 0 and the right pointer to len(newStr).

        # 3) - Then we make the usual two pointer solution with a while loop, is the character at the left pointer
        # is not the same as the character of the right pointer then is not a valid palindrome.

        # 4) - If we exit the while loop and the if statement has been not trigger then we have a valid palindrome.
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        l,r = 0, len(newStr) - 1
        while l <= r:
            if newStr[l] != newStr[r]:
                return False
            l += 1
            r -= 1
        return True