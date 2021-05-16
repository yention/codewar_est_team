# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
'''
    Given the head of a sorted linked list, delete all duplicates
    such that each element appears only once. Return the linked list sorted as well.
    Input: head = [1,1,2,3,3]
    Output: [1,2,3]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        prev = head
        curr = prev.next

        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head


if __name__ == '__main__':
    pass