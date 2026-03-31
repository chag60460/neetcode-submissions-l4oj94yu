class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw_string = re.sub(r"[^\w]", '', s.lower())
        return raw_string == raw_string[::-1]