class Solution:
    def nextPermutation(self, nums):
        n = len(nums)

        # B1: tìm i
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # B2: tìm j
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # B3: swap
            nums[i], nums[j] = nums[j], nums[i]

        # B4: đảo phần sau
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1