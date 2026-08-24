class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in range(len(strs)):
            encoded += strs[i] + "ñ"

        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        str_builder = ""

        for char in s:
            if char == "ñ":
                decoded.append(str_builder)
                str_builder = ""
            else:
                str_builder += char

        return decoded

        


