class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1) # Creating a empty list and adding the element -1.
        current = dummy # Assign the current as dummy.
        
        while list1 and list2: # Checks the list1 and list2 having values.
            if list1.val < list2.val: # Check the values of list1 is smaller than list2.
                current.next = list1 # If True means, Assign the current.next as list1
                current = list1 # Assign the current to list1.
                list1 = list1.next # Advances the list1 to its next element.
            else: # Else the values of list is not lesser then list2.
                current.next = list2 # Assign the current.next to list2.
                current = list2 # Assign the current as list2.
                list2 = list2.next # Advances the list2 to its next element.
        if list1: # If list1 still having remaining values.
            current.next = list1 # Perform the elements insertion on lists1.
        if list2:# If list2 still having remaining values.
            current.next = list2# Perform the elements insertion on lists1.
        return dummy.next # Return the dummy list 