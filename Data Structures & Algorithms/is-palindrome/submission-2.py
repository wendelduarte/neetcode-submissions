import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        padrao = r'[a-zA-Z0-9]'
        inicio = 0
        fim = len(s) -1

        inicioStr = ""
        fimStr = ""
        for i in range(0, len(s), 1):
            if re.fullmatch(padrao, s[inicio]):
                inicioStr += s[inicio].lower()
            if re.fullmatch(padrao, s[fim]):
                fimStr += s[fim].lower()
            inicio += 1
            fim -= 1
        
        return inicioStr == fimStr