class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(start, path, total):
            if total == target:
                res.append(path)
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # bỏ trùng
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                dfs(i + 1, path + [candidates[i]], total + candidates[i])

        dfs(0, [], 0)
        return res