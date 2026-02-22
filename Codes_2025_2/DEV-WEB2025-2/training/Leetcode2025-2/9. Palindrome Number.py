class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        return x == reversed_half or x == reversed_half // 10

#testes
if __name__ == "__main__":
    sol = Solution()
    test_cases = [121, -121, 10, 12321, 0, 1221, 1001]

    for num in test_cases:
        result = sol.isPalindrome(num)
        print(f"{num} -> {result}")