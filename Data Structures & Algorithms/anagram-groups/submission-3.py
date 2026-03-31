class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        frequency_to_string_hashmap = defaultdict(list)
        # key: frequency tuple
        # value: a list of strings

        for string in strs:
            
            alphabet_index_array = [0] * 26
            
            for letter in string:
                letter_index_in_ascii = ord(letter) - ord('a')
                alphabet_index_array[letter_index_in_ascii] += 1

            frequency_to_string_hashmap[tuple(alphabet_index_array)].append(string)

        return list(frequency_to_string_hashmap.values())
