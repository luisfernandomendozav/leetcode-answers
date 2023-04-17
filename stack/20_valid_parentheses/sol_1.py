class Solution:
    def isValid(self, s: str) -> bool:
        # 1. This is resolved with a stack data structure.

        # 2. First we have to create a hash table to know what bracket correspons to what bracket.

        # 3. We check if we have an open bracket, and if so we append that to our stack.

        # 4. If we dont have a opening bracket, i.e. we have a closing bracket we know that
        # we need to have a opening bracket in the top of our stack in order to be consistent.

        # 5. If we have a closing bracket and no other item on the stack we know that there is an error
        # because we cant have closing bracket without opening brackets.

        # 6. If we iterate through the string and we have an empty stack we have a valid string.
        
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        for char in s:
            if char in brackets:
                stack.append(char)
            elif len(stack) == 0 or brackets[stack.pop()] != char:
                return False
        return len(stack) == 0