class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1) - For this problem we are going to use a two pointer solution.

        # 2) - Since the numbers array is already sorted in a non-decreasing way, we know that
        # the far we move to the right the bigger the number will be.

        # 3) - So starting from l,r = 0, len(numbers)-1, we know that numbers[l] <= numbers[r].

        # 4) - Since we need to distinct index of the array the left and right pointers can not be the same,
        # so the while condition is l < r and not l <= r.

        # 5) - We calculate the total sum, and if that total sum match de target then we return the answer.

        # 6) - If not we have two possibilities, the total sum is less than the target, and the total sum is more 
        # than the target.

        # 7) - If the total sum is less than the target then we need to move our left pointer to the right because
        # thats the only way we can add more to the total sum, since every time we move to the right we increase the
        # the number.

        # 8) - If the total sum is more than the target then we need to move our right pointer to the left because
        # thats the only way we can substract to the total sum, since every time we move to the left we decrease the
        # the number.
        l,r = 0, len(numbers)-1
        while l < r:
            totalSum = numbers[l] + numbers[r]
            if totalSum == target:
                return [l+1, r+1]
            elif totalSum < target:
                l +=1
            else:
                r -= 1
        return [-1,-1]