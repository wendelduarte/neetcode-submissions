class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        response, text = "", ""
        for string in strs:
            response += str(len(string)) + ","
            text += string

        response += "#" + text
        return response


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        length_values, response, i = [], [], 0
        length = ""
        while s[i] != "#":
            j = i
            while s[j] != ",":
                length +=s[j]
                j += 1
            length_values.append(int(length))
            length = ""
            i = j + 1

        string_start = s.index("#") + 1
        
        for size in length_values:
            if (s[string_start: string_start + size] is not None):
                response.append(s[string_start: string_start + size])
            string_start += size
        return response