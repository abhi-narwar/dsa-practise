class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def removeLoop(self, head):
        slow = head
        fast = head

        # Step 1: Detect loop
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return  # No loop found

        # Step 2: Move slow to head
        slow = head

        # Step 3: Find node before loop start
        if slow == fast:
            # Loop starts at head
            while fast.next != slow:
                fast = fast.next
        else:
            # Loop starts somewhere in the middle
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next

        # Step 4: Break the loop
        fast.next = None
