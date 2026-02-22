#12/07/2025
#https://leetcode.com/problems/two-sum/description/
#MY FIRST LEETCODE
#future me nice to see you.

                            
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

if __name__ == "__main__":
    sol = Solution()
    
    #TESTING AREA! 
    nums = [3, 3, 1, 2, 3 ,2 ,1 ,2,14]
    target = 16
    result = sol.twoSum(nums, target)
    print("Result:", result)
