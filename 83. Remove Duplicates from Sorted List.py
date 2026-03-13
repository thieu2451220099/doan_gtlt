class Solution(object):
    def deleteDuplicates(self, head):
        node = head
        
        while node != None and node.next != None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
                
        return head