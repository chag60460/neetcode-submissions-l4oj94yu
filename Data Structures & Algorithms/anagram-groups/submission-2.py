class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = defaultdict(list)
        starting_index = ord('a')
        
        for string in strs:
            letter_count_array = [0] * 26

            for letter in string:
                letter_index = ord(letter) - starting_index
                letter_count_array[letter_index] += 1
                
            anagram_hash[tuple(letter_count_array)].append(string)
        
        return list(anagram_hash.values())