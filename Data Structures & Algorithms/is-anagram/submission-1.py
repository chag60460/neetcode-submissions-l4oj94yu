class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_frequency_hashmap = {}
        t_frequency_hashmap = {}

        for char in s:
            s_frequency_hashmap[char] = s_frequency_hashmap.get(char, 0) + 1
        
        for char in t:
            t_frequency_hashmap[char] = t_frequency_hashmap.get(char, 0) + 1
        
        return s_frequency_hashmap == t_frequency_hashmap

