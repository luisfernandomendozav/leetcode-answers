class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1) Okey so the first thing to do is to select a data structure
        
        # 2) I will select a hash map because is accesing the elements inside the
        #hash map is in constant time.

        # 3) I will iterate through the nums array, and I will put the elements
        # in the hash map, but before so I will check if the element is already
        # there.
        elements = {}
        for n in nums:
            if n in elements:
                return True
            elements[n] = True
        return False