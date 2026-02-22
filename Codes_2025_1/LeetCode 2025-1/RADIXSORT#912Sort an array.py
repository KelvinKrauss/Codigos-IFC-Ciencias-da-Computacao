
class Solution:
    def sortArray(self, nums):
        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2
            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i, j = left, mid
            while i < mid and j < right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            while i < mid:
                temp.append(nums[i])
                i += 1
            while j < right:
                temp.append(nums[j])
                j += 1

            nums[left:right] = temp

        merge_sort(0, len(nums))
        return nums

#testing area0_0

if __name__ == "__main__":
    solution = Solution()

    test1 = [9213, 29319, 12931, 19239, 39329, 23, 1, 2332, 123]

    print("Test 1:", solution.sortArray(test1))
