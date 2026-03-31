class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(str(len(string)) + ";" + string for string in strs)
    
    def decode(self, s: str) -> List[str]:
        current_position = 0
        decoded_string_list = []

        while current_position < len(s): 
            
            semi_colon_index = s.find(";", current_position)
            
            #everything between current position and ; position is the word length
            length = s[current_position:semi_colon_index]
            word = s[semi_colon_index+1:semi_colon_index+int(length)+1]
            decoded_string_list.append(word)
            current_position = semi_colon_index+int(length) + 1

        return decoded_string_list

        "3;app2;ab"
        "012345678"