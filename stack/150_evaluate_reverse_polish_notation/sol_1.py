class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 1 - First we have to differentiate between numbers and operators, we do by using if's

        # 2 - If those are numbers we are going to append thos to our stack.

        # 3 - Every time we encounter an operator we are going to pop the last two results,
        # since these operations always comes in pairs we are just going to pop the last two.

        # 4 - For the sum and the multiplication we have dont have problem because these,
        # operations are commutable, but we have to consider the order on the substraction and
        # division.

        # 5 - Since the strings are always a valid RPN we are going to end up with one element
        # and we return that by poping it.
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == '/':
                a,b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack.pop()