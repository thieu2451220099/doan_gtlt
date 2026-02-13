# Định nghĩa node

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        dummy = ListNode(0)   # node giả
        current = dummy      # con trỏ tạo kết quả
        carry = 0            # biến nhớ
        
        while l1 or l2 or carry:
            
            # lấy giá trị của l1
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            # lấy giá trị của l2
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            
            # tính tổng
            total = val1 + val2 + carry
            
            # cập nhật số nhớ
            carry = total // 10
            
            # tạo node mới (lấy hàng đơn vị)
            new_node = ListNode(total % 10)
            current.next = new_node
            
            # di chuyển con trỏ
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

