class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hash_map = {}

        for string in strs:
            
            anagram = "".join(sorted(string))

            #Create Key Array pair
            if anagram not in hash_map:
                hash_map[anagram] = [string]

            #Append to array
            else:
                hash_map[anagram].append(string)
        
        return list(hash_map.values())
