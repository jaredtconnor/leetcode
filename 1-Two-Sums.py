class Solution:
    def TwoSums_naive(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    def TwoSums_dict(self, nums: list[int], target: int) -> list[int]:

        counts = dict()

        for i in nums:
            couts[i] = counts.get(i, 0) + 1
