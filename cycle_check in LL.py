class Solution:                                          
    def detectLoop(self, head):
        slow, fast = head, head      #floyd's cycle detection  
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                return True
        return False
