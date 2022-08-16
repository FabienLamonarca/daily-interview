class Solution:

    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def roman_to_int(self, s: str) -> int:
        if len(s) < 1 or len(s) > 15:
            return False
        for char in s:
            if char not in self.romans.keys():
                return False

        total = 0
        last_char = None

        for i in range(len(s), 0, -1):
            char = s[i-1]
            add = self.romans.get(char)

            if last_char is not None and self.romans.get(last_char) > add:
                add = -add

            total = total + add
            last_char = char

        return total