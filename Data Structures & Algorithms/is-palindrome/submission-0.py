class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(s)
        front = 0
        end = len(s)-1
        while front <= end:
            if s[front] == s[end]:
                front += 1
                end -= 1
                continue
            else:
                return False
        return True