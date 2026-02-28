class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        closest = nums[0] + nums[1] + nums[2]  # tổng ban đầu
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                # Cập nhật nếu gần target hơn
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                # Di chuyển con trỏ
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # chính xác target
        
        return closest
    