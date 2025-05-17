"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise
input: head = [1, 2, 2, 1]
output: true
Linked List, Two Pointers, Stack, Recursion
"""
def isPal(head):
    fast = head
    slow = head
    # find middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    # reverse second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    # check palindrome
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

def isPalindrome(head):
    vals = []
    current = head
    while current is not None:
        vals.append(current.val)
        current = current.next
    return vals == vals[::-1]
# time complexity: o(n)
# space complexity: o(n)

def isPalindrome2(self, head: ListNode):
    self.front_pointer = head

    def recursively_check(current_node=head):
        if current_node is not None:
            if not recursively_check(current_node.next):
                return False
            if self.front_pointer.val != current_node.val:
                return False
            self.front_pointer = self.front_pointer.next
        return True

    return recursively_check()
# time: o(n)
# space: o(n)

def isPalindrome3(self, head: ListNode) -> bool:
    if head is None:
        return True

    # Find the end of first half and reverse second half.
    first_half_end = self.end_of_first_half(head)
    second_half_start = self.reverse_list(first_half_end.next)

    # Check whether or not there's a palindrome.
    result = True
    first_position = head
    second_position = second_half_start
    while result and second_position is not None:
        if first_position.val != second_position.val:
            result = False
        first_position = first_position.next
        second_position = second_position.next

    # Restore the list and return the result.
    first_half_end.next = self.reverse_list(second_half_start)
    return result

def end_of_first_half(self, head: ListNode) -> ListNode:
    fast = head
    slow = head
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow

def reverse_list(self, head: ListNode) -> ListNode:
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous
# time complexity: o(n)
# space complexity: o(1)