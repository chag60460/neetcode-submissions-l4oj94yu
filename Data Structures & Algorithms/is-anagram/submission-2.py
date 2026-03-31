class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        frequency_hashmap = {}

        for char in s:
            frequency_hashmap[char] = frequency_hashmap.get(char, 0) + 1
        
        for char in t:
            frequency_hashmap[char] = frequency_hashmap.get(char, 0) - 1
        
        return all(count == 0 for count in frequency_hashmap.values())

