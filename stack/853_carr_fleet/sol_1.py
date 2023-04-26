class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # 1 - First we are going to combine the two arryas into one using
        # the zip method.

        # 2 - Then we are going to sort using the position value with the sorted
        # method.

        # 3 - We are going to start from the top to the bottom, calculating at what time
        # the car that is at the top of the stack arrives at the target, and we are going to append
        # that to our stack data structure.

        # 4 -  Then we are going to compare in pairs, the last with the one before last, if the
        # time of the one before the last one is less than the last one, that means that in some
        # point the two are going to colide, so we can treat this two as one, thats why we pop.

        # 5 - The number of fleets its going to be the number of items left in the stack.
        pair = [[p, s] for p,s in zip(position, speed)]
        stack = []
        print(sorted(pair))
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)