class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    # Function to check if the linked list has a loop
    def cycle_check(self, head):                                    '''in this question we take two pointer marker1 as as slow pointer which moves one step and marker2 as fast pointer which moves 2 steps ,we iterate over the entire list using while loop  
        marker1 = head                                               '''
        marker2 = head

        while marker2 !=None and marker2.next !=None:
            marker1 = marker1.next
            marker2 = marker2.next.next

            if marker1 == marker2:
                return True

        return False

# Creating nodes
node1 = Node(1)
node2 = Node(3)
node3 = Node(4)

# Linking nodes with a loop
node1.next = node2
node2.next= node3
node3.next = node2  # Loop here

# Creating Solution object and checking for loop
s = Solution()
s.cycle_check(node1)  # Output: True
