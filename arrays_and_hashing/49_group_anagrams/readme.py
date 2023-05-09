class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashM = defaultdict(list)
        while len(strs) > 0:
            st = strs.pop()
            
            signature = [0]*26
            for s in st:
                signature[ord(s) - ord('a')] += 1
            hashM[tuple(signature)].append(st)
        
        return hashM.values()
        """
        Alternative solution almost the same but with using a stack

        # This is the same solution as the first solution but using a default dictionary
        # In this case we use empty lists as values for our dictionary
        hM = defaultdict(list)
        # Iterate over the strings array.
        for st in strs:
            count = [0]*26
            for c in st:
                count[ord(c) - ord('a')] += 1
            hM[tuple(count)].append(st)
        return hM.values()

        """
