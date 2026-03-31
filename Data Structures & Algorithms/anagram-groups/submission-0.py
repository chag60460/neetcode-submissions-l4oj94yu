class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #Keep track of sorted string and their combinations
        anagram_hash = {} #key: sprted string, #value: array of strings in strs

        for string in strs:

            #sort string
            key = ''.join(sorted(string))

            #add key if not in hashmap already
            if key not in anagram_hash:
                anagram_hash[key] = []
            
            anagram_hash[key].append(string)

        return list(anagram_hash.values())