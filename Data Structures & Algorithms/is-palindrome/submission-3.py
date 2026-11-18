class Solution:
    def isPalindrome(self, s: str) -> bool:
        inicio = 0
        fim = len(s) -1

        inicioStr = ""
        fimStr = ""
        for i in range(0, len(s), 1):
            if  s[inicio].isalnum():
                inicioStr += s[inicio].lower()
            if  s[fim].isalnum():
                fimStr += s[fim].lower()
            inicio += 1
            fim -= 1
        
        return inicioStr == fimStr