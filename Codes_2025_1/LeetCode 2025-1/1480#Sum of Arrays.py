class Solution(object):
    def runningSum(self, nums):
        res = []
        total = 0
        for num in nums:
            total += num
            res.append(total)
        return res

s = Solution()
print(s.runningSum([1, 2, 3, 4]))