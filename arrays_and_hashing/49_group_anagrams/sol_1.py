class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1) - So for this problem we have an input like this:
        # ["eat","tea","tan","ate","nat","bat"], and wee need to generate
        # an out put like this: [["bat"],["nat","tan"],["ate","eat","tea"]]

        # 2) - We need to group all the strings that are anagrams i.e. that
        # we can form those strings with the same letters and the same number
        # of letters.

        # 3) - We identify that, If a word is an anagram of another word
        # then they have the same number of letters and the same ones, so
        # we can generate an array with the number of letters per position,
        # assuming that for position 0, corresponds letter 'a', for position 1
        # corresponds letter 'b', for position 3 corresponds letter 'c', and so on.

        # 4) - We know that we have 26 letters in the alphabet from 'a' to 'z', we can
        # usea an array of length 26 for this.

        # 5) - Then we are going to use the ascii value using the function 'ord' and
        # we are goint to reference the letter a for this, so ord('a') - ord('b') = 0,
        # ord('b') - ord('a) = 1, ord('c') - ord('a') = 2, and so on.

        # 6) - Then for example If I try to generate this array for the word 'eat' we will have
        # something like this: [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        # This                 (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
        # We see that we have a +1 were we have a letter, if in the string we had two letter 'a'       
        # we'll have a 2, were the letter 'a' corresponds.

        # 7) - Then we will use this array as a key for our hash map, but in the form of a tuple,
        # since we can not use arrays as keys, so will have something like this:
        # hM = {(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0): ['eat']}

        # 8) - So after this if we get the word 'ate' we will have the same signature array:
        # [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
        # (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
        # so we will have on the hash map:
        # hM = {(1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0): ['eat', 'ate']} and so on.


        # We initialize the hash map.
        hM = {}
        # Iterate over the strings array.
        for st in strs:
            # Generate a 26 length array with just zeros.
            count = [0]*26
            for c in st:
                # We add one on the position that corresponds to character c.
                count[ord(c) - ord('a')] += 1
            # We use a tuple because we can not use an array.
            # If the tuple key is not in the hash keys we add an array with the current string.
            if tuple(count) not in hM:
                hM[tuple(count)] = [st]
            # If the tuple key already exists that means that we have an array in there, so we just append the current string.
            else:
                hM[tuple(count)].append(st)
        # Then we just return the values of the hash map.
        return hM.values()