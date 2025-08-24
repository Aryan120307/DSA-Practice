class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]   # return indices
        return []  # if no pair is found


nums = [1, 2, 3, 5, 6, 7, 8, 9, 10]
target = 5
Sol = Solution()
print(Sol.twoSum(nums, target))
