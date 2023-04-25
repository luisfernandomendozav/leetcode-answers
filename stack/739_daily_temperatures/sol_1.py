class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1 - First have to iterate over the temperature array.

        # 2 - Then we are going to define a stack data structure, were we are going,
        # to store the idx and the temperature.

        # 3 - We need a response array as well, that we are going to fill with zeros, because
        # that is the default value.

        # 4 - Then the first time we iterate we are going to append the first temperature of the
        # temperature array, its index and the actual value

        # 5 - If we have a couple of values in the stack, we are going to compare the top 
        # item of the stack with the current value we are iterating.

        # 6 - if the temperature of the current value is greater than the temperature of the top of
        # top of the stack, we are going to pop that value and fill the corresponding place in the
        # response array, and we are going to keep doing that untill we dont have any more items
        # on the stack or we encounter a greater temperature than the actual one.

        # 7 - Then we are going to append the current item to the stack.


        stack = []
        res = [0]*len(temperatures)

        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][1]:
                index, temperature = stack.pop()
                res[index] = idx - index
            stack.append([idx,temp])
        return res

        
        """
        Brute Force solution that works for small tempratures arrays
        
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            l,r = i,i+1
            while r < len(temperatures):
                if temperatures[l] < temperatures[r]:
                    res[l] += r - l
                    break
                else:
                    r +=1
        return res

        """

