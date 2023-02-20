class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1) - First we have to create a post fix and a pre fix array.

        # 2) - The post fix array i.e. the array that contain all the multiplications after a given index i.e [1,2,3,4,5] => [120,120,60,20,5]

        # 3) - The pre fix array i.e. the array that contain all the multiplications before a given index i.e [1,2,3,4,5] => [1,2,6,24,125]
        
        # 4) - Then the response array is calculated by multiplying the index before of the pre fix array times the index after the post fix array i.e res[i] = [preFix[i-1], postFix[i+i]

        # 5) - Since the prefix and postfix arrays have the same length of the response array we will have prefix[-1] and a postfix[length(postFix)] i.e. out of bounds index,
        # for this edge cases we will treat this as they were one i.e. prefix[-1]=1 and postfix[length(postFix)] = 1
        
        postFix = []
        tmp = 1
        # We calculate the postfix array
        for n in nums[::-1]:
            postFix.insert(0,n*tmp)
            tmp *= n
        
        preFix = []
        tmp = 1
        # we calculate the prefix array
        for n in nums:
            preFix.append(tmp*n)
            tmp *= n
        res = []
        # we form the response array taking into account the edge cases
        for i in range(len(preFix)):
            # edge case for prefix[-1]
            if i == 0:
                pre = 1
            else:
                pre = preFix[i-1]
            # edge for postfix[length(preFix)] remember that prefix and postfix have the same length
            if i == len(preFix) - 1:
                post = 1
            else:
                post = postFix[i+1]
            
            res.append(pre*post)
        return res
        