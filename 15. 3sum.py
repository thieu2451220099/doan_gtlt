class Solution(object):
    def threeSum(self, nums):
        nums.sort()  # Sắp xếp mảng
        result = []
        n = len(nums)
        
        for i in range(n - 2):
            # Bỏ qua số trùng lặp
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Nếu số hiện tại > 0 thì dừng (vì mảng đã sort)
            if nums[i] > 0:
                break
            
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Bỏ qua trùng lặp bên trái
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                        
                    # Bỏ qua trùng lặp bên phải
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                    
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return result