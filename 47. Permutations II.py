class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                res.append(path)
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # bỏ trùng
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                dfs(path + [nums[i]])
                used[i] = False

        dfs([])
        return res