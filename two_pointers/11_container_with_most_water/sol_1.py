class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 1) - This is a two pointer problem, we define the l and r pointers.

        # 2) - We calculate the area as (r - l) * min(height[l],height[r]),
        # we take minimum of height[l] and height[r] because after the minimum
        # height the water just spills.

        # 3) - We compare the are that we just compute vs the global max area
        # and we take the max of this two.

        # 4) - We move the pointer with the shorter height because thats the one
        # that is limiting how much water we can store.

        # 5) - If the height are equals we can choose either way thats why we
        # put the condition as '<='.
        

        l,r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            area = (r - l) * min(height[l],height[r])
            maxArea = max(maxArea, area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea