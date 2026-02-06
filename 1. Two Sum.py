class Solution:
    def twoSum(self, nums, target):
        t = {}

        for i in range(len(nums)):
            n = nums[i]
            s = target - n

            if s in t:
                return [t[s], i]
            t[n] = i