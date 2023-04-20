class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 1 - For this probem we are going to use recursion.

        # 2 - The stack will be to keep track of how we append all the parentheses
        # on each level of the backTrack call.

        # 3 - Thats why when openN == closeN == n we append all the prentheses inside.

        # 4 - So one of the condition is that we can add at most n open and close parentheses

        # 5 - The other condition is that we can just add close parentheses when closeN is less than
        # openN.

        # 6 - In the first condition if openN is less than n, then we append a open parentheses
        # and go one level deep calling the function another time.

        # 7 - After we return from the backTrack recursive function, we need to pop the open parentheses
        # to go up one level until we can add a close parentheses.

        # 8 - The same with the second condition but this just checks if closeN is less than openN.

        # 9 - Then we initialize the backTrack function and return res.
        stack = []
        res = []
        def backTrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                backTrack(openN, closeN + 1)
                stack.pop()
        backTrack(0,0)
        return res