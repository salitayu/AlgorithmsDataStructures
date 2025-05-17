"""
143 Reorder List Medium Topics Linked List, Two Pointers, Stack, Recursion
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
def reorderList(head):
    if not head:
        return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev
    while second.next:
        first.next, first = second, first.nexts
        second.next, secon = first, second.next
    # time O(n)
    # space O(1)