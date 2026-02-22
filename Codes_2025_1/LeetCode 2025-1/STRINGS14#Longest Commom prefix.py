#https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=string
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:

            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
    
#LOCAL TESTS!0_0
if __name__ == "__main__":
    sol = Solution()
    
    #test 1
    strs1 = ["cute sheep", "cute andorinha", "cute backiardigans"]
    print("Test 1:", sol.longestCommonPrefix(strs1))  # Output: "fl"

    