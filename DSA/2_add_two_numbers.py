r"""
=====================================================================
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/
=====================================================================

FIRST: WHAT IS A LINKED LIST? (read this before the problem)
============================================================
So far every problem used a Python LIST (an array): items sitting in one
continuous row, reachable instantly by index (nums[3]).

A LINKED LIST is different. It is a chain of little boxes called NODES.
Each node holds TWO things:
    1) a value  (the data, e.g. a digit)
    2) a "next" arrow pointing to the NEXT node (or to nothing at the end)

    [2] -> [4] -> [3] -> None
     ^val  ^val   ^val   ^"None" means "end of the chain, no next node"

You do NOT get instant index access. To reach the 3rd node you must start at
the 1st and follow the arrows: node, node.next, node.next.next. You walk the
chain one hop at a time.

A single node in Python looks like this (LeetCode gives you this class):

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val      # the data in this box
            self.next = next    # arrow to the next box (None = end)

To build [2,4,3] by hand:
    a = ListNode(2)
    b = ListNode(4)
    c = ListNode(3)
    a.next = b      # 2 -> 4
    b.next = c      # 4 -> 3   (c.next stays None = end)
    # `a` is the HEAD (first node); from it you can reach the whole chain.

WHY linked lists exist (vs arrays):
    - Inserting/removing in the MIDDLE is cheap: just re-point a couple arrows,
      no shifting of everything like an array needs.
    - Cost: no instant nums[i]; you must walk from the head. Also more memory
      per item (each node stores an extra arrow).

HEAD / TRAVERSAL words:
    - HEAD: the first node. If you lose it, you lose the whole list.
    - TRAVERSE / WALK: follow .next over and over until you hit None.
        node = head
        while node is not None:
            ...use node.val...
            node = node.next      # hop to the next box


THE PROBLEM (in plain words)
============================
Two numbers are given as linked lists, with digits in REVERSE order
(ones digit first). Add them, return the sum as a linked list (also reversed).

    l1 = 2 -> 4 -> 3   represents the number 342  (read backwards: 3,4,2)
    l2 = 5 -> 6 -> 4   represents the number 465
    342 + 465 = 807
    answer = 7 -> 0 -> 8   (807 backwards)

Reverse order is actually HELPFUL: the ones digits are first, so we can add
left to right just like adding by hand on paper, carrying as we go.


THE KEY IDEA: add digit by digit with a CARRY (grade-school addition)
---------------------------------------------------------------------
Walk both lists together. At each step:
    total = digit_from_l1 + digit_from_l2 + carry_from_previous_step
    new_digit = total % 10     # the ones part stays in this node
    carry     = total // 10    # the tens part (0 or 1) moves to the next step
Make a new node holding new_digit. Continue until BOTH lists are done AND
there is no leftover carry.

    Example: 99 + 1  ->  l1 = 9->9,  l2 = 1
      step1: 9 + 1 + 0 = 10 -> digit 0, carry 1   (node 0)
      step2: 9 + 0 + 1 = 10 -> digit 0, carry 1   (node 0)
      step3: 0 + 0 + 1 = 1  -> digit 1, carry 0   (node 1)  <- extra node!
      result = 0 -> 0 -> 1   (which is 100, correct)
    That final carry creates an EXTRA node -- a classic edge case.


THE DUMMY HEAD TRICK (makes building the result list painless)
--------------------------------------------------------------
When building a NEW linked list, the first node is awkward: you have nothing
to attach it to yet. The fix: create a throwaway "dummy" node FIRST and build
after it. At the end, the real answer is dummy.next (skip the dummy). This
avoids a special "is this the first node?" check on every step.

    dummy = ListNode()      # placeholder, value ignored
    tail = dummy            # `tail` always points at the last real node so far
    ... tail.next = new_node ; tail = tail.next ...
    return dummy.next       # the chain we actually built


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    1..100 nodes per list
    0 <= Node.val <= 9          (each node is a single digit)
    no leading zeros (except the number 0 itself, which is just [0])


EDGE CASES (unusual inputs to check)
------------------------------------
- Different lengths: [9,9,9,9,9,9,9] + [9,9,9,9]  (one list runs out early)
- Final carry adds a new node: [5] + [5] -> [0,1]  (5+5=10)
- Zeros: [0] + [0] -> [0]
- One number much longer than the other.


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Time  O(max(m, n)): we walk each list once, m and n = their lengths.
- Space O(max(m, n)): the result list is about that long (+1 if final carry).
"""

from typing import Optional   # "Optional[ListNode]" = a ListNode OR None (the end)


# LeetCode pre-defines this for you. We define it here so this file runs
# locally on its own.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # the digit stored in this node
        self.next = next    # arrow to the next node (None marks the end)


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: iterate with a dummy head + carry  (THE answer -- learn this)
    # ----------------------------------------------------------------
    #
    # `l1`, `l2` are the HEAD nodes of the two input chains.
    # We walk both at once, summing digits with a carry, and append each new
    # digit node onto a result chain built after a dummy node.
    #
    # The loop runs while EITHER list still has nodes OR a carry remains -- that
    # last part is what lets a trailing carry create the extra final node.
    #
    # Time: O(max(m, n))   Space: O(max(m, n))
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # throwaway head; real answer is dummy.next
        tail = dummy            # tail = last node of the result so far
        carry = 0               # leftover to add into the next column

        # keep going while there is anything left to add (digits OR a carry)
        while l1 is not None or l2 is not None or carry != 0:
            # if a list ran out, treat its missing digit as 0
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            total = x + y + carry
            carry = total // 10         # 0 or 1: moves to the next column
            digit = total % 10          # the digit that stays here

            tail.next = ListNode(digit) # attach a new node holding this digit
            tail = tail.next            # advance the tail to it

            # hop forward in each list IF it still has nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return dummy.next               # skip the dummy -> the real chain

    # ----------------------------------------------------------------
    # SOLUTION 2: recursion  (same math, expressed as "solve the rest")
    # ----------------------------------------------------------------
    #
    # RECURSION = a function that calls ITSELF on a smaller piece of the problem.
    # Here: add the current two digits (+ carry), then ask the SAME function to
    # add the rest of the two lists, passing along the new carry. It stops (the
    # "base case") when both lists are empty and there is no carry left.
    #
    # Many people find the loop (Solution 1) easier; recursion is shown so you
    # see the alternative. Note: deep recursion can hit Python's recursion limit
    # for very long lists (here max 100 nodes, so it's fine).
    #
    # Time: O(max(m, n))   Space: O(max(m, n)) for the result + call stack
    def addTwoNumbers_recursive(self, l1, l2, carry=0):
        # base case: nothing left in either list and no carry -> end of chain
        if l1 is None and l2 is None and carry == 0:
            return None

        x = l1.val if l1 is not None else 0
        y = l2.val if l2 is not None else 0
        total = x + y + carry

        node = ListNode(total % 10)     # this digit
        # build the rest by recursing on the next nodes, carrying total // 10
        next_l1 = l1.next if l1 is not None else None
        next_l2 = l2.next if l2 is not None else None
        node.next = self.addTwoNumbers_recursive(next_l1, next_l2, total // 10)
        return node


# =====================================================================
# HELPERS for local testing (convert between Python list and linked list)
# =====================================================================
# These are NOT part of the solution -- just so we can test easily on our
# machine by turning [2,4,3] into a real chain and back.

def build_linked_list(values):
    """Turn a Python list like [2,4,3] into a linked list, return its head."""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next   # head (or None if values was empty)


def linked_list_to_pylist(head):
    """Turn a linked list back into a Python list like [2,4,3]."""
    out = []
    node = head
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


# =====================================================================
# LOCAL TESTING
# =====================================================================
if __name__ == "__main__":
    s = Solution()

    # Each entry: (l1 values, l2 values, expected result values)
    tests = [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),                         # 342 + 465 = 807
        ([0], [0], [0]),                                           # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
        ([5], [5], [0, 1]),                                        # 5 + 5 = 10 -> extra node
        ([1, 8], [0], [1, 8]),                                     # 81 + 0 = 81
    ]

    # Iterative version
    for l1v, l2v, expected in tests:
        head = s.addTwoNumbers(build_linked_list(l1v), build_linked_list(l2v))
        assert linked_list_to_pylist(head) == expected, f"iterative failed on {l1v},{l2v}"

    # Recursive version
    for l1v, l2v, expected in tests:
        head = s.addTwoNumbers_recursive(build_linked_list(l1v), build_linked_list(l2v))
        assert linked_list_to_pylist(head) == expected, f"recursive failed on {l1v},{l2v}"

    print("all tests pass")
