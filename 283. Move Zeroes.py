class Solution:
    def moveZeroes(self, nums):
        j = 0  # vị trí đặt số khác 0
        
        # Đưa các số ≠ 0 lên trước
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        
        # Fill 0 phía sau
        for i in range(j, len(nums)):
            nums[i] = 0