class Solution(object):
    def middleNode(self, head):
        fast = slow = head # Assigning the fast and slow as head.
        while fast and fast.next: # Iterate through each head element.
            fast , slow = fast.next.next, slow.next # Assigning the fast and slow element with the upcoming elements.
        return slow # Return the slow at the end