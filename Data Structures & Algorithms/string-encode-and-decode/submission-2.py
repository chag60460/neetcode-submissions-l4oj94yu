class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        
        for string in strs:
            encoded_string += str(len(string)) + "#" + string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_array = []
        number_index = 0

        while number_index < len(s):

            hashtag_index = number_index
            while s[hashtag_index] != "#":
                hashtag_index += 1

            #Compute Varaibles
            string_length = int(s[number_index:hashtag_index])
            start_of_string = hashtag_index + 1
            end_of_string = start_of_string + string_length

            #Extract Word
            word = s[start_of_string : end_of_string]
            decoded_array.append(word)

            #Start at the next word
            number_index = end_of_string
        
        return decoded_array