import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        inicio = 0
        fim = len(s) -1

        inicioStr = ""
        fimStr = ""
        for i in range(0, len(s), 1):
            inicioStr += s[inicio].lower()
            fimStr += s[fim].lower()
            inicio += 1
            fim -= 1
        
        return inicioStr == fimStr