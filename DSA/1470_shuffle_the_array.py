r"""
=====================================================================
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
You get a list that is secretly TWO halves stuck together.
The first half is the "x" numbers, the second half is the "y" numbers.

    nums = [2, 5, 1,  3, 4, 7],  n = 3
            \-----/   \-----/
            x's        y's
            x1=2 x2=5 x3=1   y1=3 y2=4 y3=7

You must INTERLEAVE them (zip them together) like a zipper:
    take x1, then y1, then x2, then y2, then x3, then y3
    result = [2, 3, 5, 4, 1, 7]
              x1 y1 x2 y2 x3 y3


WORDS / IDEAS YOU NEED
----------------------
- `n`:
  How many pairs there are. The whole list has 2*n items.
  The x's live at positions 0 .. n-1.
  The y's live at positions n .. 2n-1.
  So for any pair number i (0,1,2,...):
        the x of that pair is at index  i
        the y of that pair is at index  i + n   <-- jump forward by n to reach its partner

- WHY i + n REACHES THE PARTNER:
  x1 is at index 0, its partner y1 is at index 0+n.
  x2 is at index 1, its partner y2 is at index 1+n. And so on.
  This "+n jump" is the heart of the whole problem.

- INTERLEAVE / ZIP:
  Lay two rows side by side and read them in a criss-cross:
  x1, y1, x2, y2, ...  That alternating read is the answer.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    1 <= n <= 500          -> there is always at least 1 pair
    nums.length == 2n      -> the list is always exactly 2*n long (even length)
    1 <= nums[i] <= 1000   -> values don't matter to the logic; it's about POSITIONS


EDGE CASES (unusual inputs to check)
------------------------------------
- Smallest input: n == 1, e.g. [a, b] -> [a, b]  (one pair, nothing really moves)
- Repeated values, e.g. [1,1,2,2], n=2 -> [1,2,1,2]. Works fine: we move by
  POSITION, we never care whether two values look the same.


SPEED & MEMORY (time / space complexity)
----------------------------------------
- We must produce 2*n numbers, so we always do work proportional to n.
- Time  O(n): work grows in a straight line with the input size.
- Space O(n): the answer list holds 2*n numbers.
  (You CAN do it in O(1) extra space with bit-tricks, but that is advanced
   and not worth it here -- clarity beats cleverness in an interview for an
   easy problem.)
"""

from typing import List   # type hint helper: lets us write "List[int]" = list of ints


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: plain loop with the "+ n" jump  (clearest to explain)
    # ----------------------------------------------------------------
    #
    # Walk one pair at a time. For pair number i:
    #   - the x value is nums[i]
    #   - its partner y value is nums[i + n]   (jump forward by n)
    # Add x then y to the answer, in that order. Repeat for every pair.
    #
    # Reading the header:
    #   nums: List[int]  -> the input list of integers
    #   n: int           -> a single whole number (how many pairs)
    #   -> List[int]     -> we return a list of integers
    #
    # Time: O(n)   Space: O(n)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []                      # start with an empty answer list
        for i in range(n):            # i takes values 0, 1, 2, ..., n-1 (each pair)
            ans.append(nums[i])       # add the x of this pair  (front half)
            ans.append(nums[i + n])   # add the y of this pair  (back half, +n jump)
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 2: pre-size the answer and write to exact slots
    # ----------------------------------------------------------------
    #
    # Same idea, but instead of appending we make the answer full-size up front
    # (filled with placeholder zeros) and drop each number into its exact slot.
    #
    # Where does each number go in the answer?
    #   For pair i, x goes to answer position 2*i,
    #               y goes to answer position 2*i + 1.
    #   (pair 0 -> slots 0,1 ; pair 1 -> slots 2,3 ; pair 2 -> slots 4,5 ...)
    #   The "2*i" pattern is what creates the x,y,x,y,... alternation.
    #
    # Time: O(n)   Space: O(n)
    def shuffle_index(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)           # make a list of 2*n zeros to overwrite
        for i in range(n):
            ans[2 * i] = nums[i]          # x of pair i -> even slot
            ans[2 * i + 1] = nums[i + n]  # y of pair i -> next (odd) slot
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 3: Python's zip + slicing  (short & idiomatic)
    # ----------------------------------------------------------------
    #
    # Two new tools here:
    #
    # 1) SLICING -- `nums[start:stop]` gives a sub-list from index `start` up to
    #    (but NOT including) `stop`.
    #       nums[:n]  = "from the beginning up to n"  = the x half
    #       nums[n:]  = "from n to the end"           = the y half
    #
    # 2) zip(a, b) -- pairs up two lists item by item:
    #       zip([2,5,1], [3,4,7]) gives the pairs (2,3), (5,4), (1,7)
    #    Exactly the x/y partners we want.
    #
    # Then for each (x, y) pair we add both to the answer.
    #
    # Time: O(n)   Space: O(n)
    def shuffle_zip(self, nums: List[int], n: int) -> List[int]:
        xs = nums[:n]                 # first half  -> the x numbers
        ys = nums[n:]                 # second half -> the y numbers
        ans = []
        for x, y in zip(xs, ys):      # walk both halves together as (x, y) pairs
            ans.append(x)             # x first
            ans.append(y)             # then its partner y
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 4: one-line version of Solution 3  (compact; know how it reads)
    # ----------------------------------------------------------------
    #
    # This is a "list comprehension" -- a compact way to build a list with a
    # loop written inside the [ ] brackets. Read it as:
    #   "for each (x, y) pair from zip(...), and for each value v in [x, y],
    #    collect v"  -> which produces x, y, x, y, ...
    # Powerful but harder to read; fine to prefer Solution 1 in an interview.
    #
    # Time: O(n)   Space: O(n)
    def shuffle_oneline(self, nums: List[int], n: int) -> List[int]:
        return [v for x, y in zip(nums[:n], nums[n:]) for v in (x, y)]


# =====================================================================
# LOCAL TESTING
# =====================================================================
# This block runs ONLY when you run this file directly (python <file>.py).
# It is our own check that all four solutions give the right answers.
# (On LeetCode, their own hidden driver calls `shuffle` instead; this block
#  is ignored there -- that's what `if __name__ == "__main__"` controls.)
if __name__ == "__main__":
    s = Solution()

    # Each entry: (input list, n, expected output)
    tests = [
        ([2, 5, 1, 3, 4, 7],       3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2],             2, [1, 2, 1, 2]),
        ([9, 8],                   1, [9, 8]),   # edge: smallest input, one pair
    ]

    methods = [
        s.shuffle,
        s.shuffle_index,
        s.shuffle_zip,
        s.shuffle_oneline,
    ]

    for nums, n, expected in tests:
        for m in methods:
            # list(nums) passes a fresh copy so one method can't disturb the next
            assert m(list(nums), n) == expected, f"{m.__name__} failed on {nums}"

    print("all tests pass")
