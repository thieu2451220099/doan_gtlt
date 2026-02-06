class Solution(object):
    def removeDuplicates(self, nums):
        # Nếu mảng rỗng
        if not nums:
            return 0

        k = 1  # Vị trí ghi phần tử duy nhất tiếp theo

        # Duyệt từ phần tử thứ 2
        for i in range(1, len(nums)):
            # Nếu khác phần tử trước đó → là số mới
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
