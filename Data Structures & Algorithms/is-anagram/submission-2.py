class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash = Counter(s)
        t_hash = Counter(t)

        for char, quantity in s_hash.items():
            if char not in t_hash or t_hash.get(char) != quantity:
                return False
        return True
