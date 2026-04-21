class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        for ch in s:
            if ch == " ":
                continue
            if not (("A" <= ch <= "Z") or ("a" <= ch <= "z") or ch.isnumeric()):
                continue
            if ch.isupper():
                str+=ch.lower()
            else:
                str+=ch
        val=""
        for i in range((len(str)-1),-1,-1):
            val+=str[i]
        if val==str:
            return True
        else:
            return False
