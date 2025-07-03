class Solution:
    def removeLoop(self, head):
        # If list is empty or has only one node, then no loop possible
        if head is None or head.next is None:
            return

        # Step 1: Use two pointers (slow and fast) to detect loop
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next         # move slow by 1 step
            fast = fast.next.next    # move fast by 2 steps

            if slow == fast:         # if slow and fast meet, loop is present
                break

        # If no loop found (fast reached end), return
        if fast is None or fast.next is None:
            return

        # Step 2: Move slow back to start (head)
        slow = head

        # Step 3: Move slow and fast one step at a time
        # They will meet at the starting point of the loop
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Step 4: Move fast to the last node of the loop
        # (the node whose next is pointing to the starting point of loop)
        while fast.next != slow:
            fast = fast.next

        # Step 5: Break the loop by setting fast.next to None
        fast.next = None
