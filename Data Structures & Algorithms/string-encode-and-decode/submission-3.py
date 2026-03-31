class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_array = []
        starting_index = 0
        hashtag_index = 0
        
        while hashtag_index < len(s):
            hashtag_index += 1
            
            #Read until we see #, extract the number
            #Use this number as length and fetch the string
            if s[hashtag_index] == "#":
                length = int(s[starting_index : hashtag_index])
                string = s[hashtag_index + 1 : hashtag_index + 1 + length]
                decoded_array.append(string)

                starting_index = hashtag_index + length + 1
                hashtag_index = starting_index

        return decoded_array