class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 1) - First we assign each array to a variable.
        
        # 2) - We need to know what is the total length of the two arrays
        # and the half of the two arrays combined.
        # 3) - Then we need to identify the shortest array between these two.
        # 4) - We know that A is the shortest array, so we are going to start with binary search
        # with A.
        # 5) - This is the middle pointer for A mA = middle A.
        # 6) - This is the middle pointer for B mB = middle B, we calculate the middle
        # point of B through A, we take the half of the two arrays combined and substract the
        # half of A minus 2 because the two arrays start from 0.
        A,B = nums1,nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(B) < len(A):
            A,B = B,A
        
        l,r = 0, len(A) - 1
        while True:
            
            mA = (l + r) // 2
            mB = half - mA - 2

            Aleft = A[mA] if mA >= 0 else float("-infinity")
            
            Aright = A[mA + 1] if (mA+1) < len(A) else float("infinity")
            
            Bleft = B[mB] if mB >= 0 else float("-infinity")
            
            Bright = B[mB + 1] if (mB+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mA - 1
            else:
                l = mA + 1
                