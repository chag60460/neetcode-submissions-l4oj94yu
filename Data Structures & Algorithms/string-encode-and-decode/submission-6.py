class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"#{len(string)}#{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        start = 0
        end = 1
        decoded = []

        while end < len(s):
            if s[end] == "#":
                string_length = int(s[start+1:end])
                decoded.append(s[end + 1 : end + string_length + 1]) 
                start = end + string_length + 1
                end = start + 1
            end += 1
        
        return decoded