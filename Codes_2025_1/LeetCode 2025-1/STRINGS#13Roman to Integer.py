#create string for Roman: I, V, X, L, C, D, M.
#(I=1)(V=5)(X=10)(L=50)(C=100)(D=500)(M=1000)
#logic of line 25-28
#looping through each character in the Roman numeral string s, one by one, using its index i
#checks if the current Roman character is part of a subtractive pair
#if the above condition is true, we subtract the current value.
#if it's not a subtractive case, just add the current value.
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total


#test area, put the roman number in the ("")) on line 28
if __name__ == "__main__":
    sol = Solution()
    print(":", sol.romanToInt("V"))      