class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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