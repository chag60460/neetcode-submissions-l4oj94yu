class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoded in # + string + len(string)
        return "".join(f"{len(string)}#{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        starting_index = 0
        hashtag_tracking_index = 0
        output = []
        
        while hashtag_tracking_index < len(s):
            
            if s[hashtag_tracking_index] == "#":
                length = int(s[starting_index:hashtag_tracking_index])
                string = s[hashtag_tracking_index + 1: hashtag_tracking_index + length + 1]
                output.append(string)

                starting_index = hashtag_tracking_index + length + 1
                hashtag_tracking_index = starting_index

            else:
                hashtag_tracking_index += 1

        return output