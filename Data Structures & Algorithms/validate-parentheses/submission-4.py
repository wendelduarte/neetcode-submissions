class Solution:
    def isValid(self, s: str) -> bool:
        charsOpen = ["(", "{", "["]
        charsClose = [")", "}", "]"]
        charToClose = []

        if len(s) % 2 != 0:
            return False

        if not any(item in s for item in charsOpen):
            return False

        if not any(item in s for item in charsClose):
            return False

        for char in s:
            if char in charsClose:
                if not charToClose:
                    return False
                else:
                    if char != charToClose[-1]:
                        return False
                    else:
                        charToClose.pop()
            if char in charsOpen:
                charToClose.append(charsClose[charsOpen.index(char)])
        
        if not charToClose:
            return True
        else:
            return False
                
            
                