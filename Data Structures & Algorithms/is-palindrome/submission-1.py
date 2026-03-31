class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_string = re.sub(r'[\W_]+', '', s.lower())
        print(raw_string)
        print(raw_string[len(raw_string)-1:-1:-1])
        return raw_string == raw_string[::-1]