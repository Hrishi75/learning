r"""
=====================================================================
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
Imagine you SHOULD have the numbers 1, 2, 3, ..., n -- each exactly once.
But one number got copied over another. So now:
  - one number appears TWICE (the duplicate), and
  - one number is MISSING (the one that got overwritten).

You are given the broken list `nums`. Return [duplicate, missing].

    nums = [1, 2, 2, 4]     should have been {1,2,3,4}
              ^  ^           2 appears twice
                      and 3 never appears
    answer = [2, 3]         -> [the duplicate, the missing one]


WORDS / IDEAS YOU NEED
----------------------
- n:
  The list length. The numbers SHOULD be 1..n. For [1,2,2,4], n = 4,
  so the correct set is {1,2,3,4}.

- DUPLICATE: the value that shows up two times.
- MISSING:   the value from 1..n that shows up zero times.

- HASH / FREQUENCY COUNT (a BIG new idea):
  "How many times does each number appear?" To answer that fast, we COUNT.
  We keep a little tally for every number. Two common tools:
    * a dictionary (a.k.a. hash map): pairs of  value -> how many times seen
    * a plain counting array: a row of tallies, one slot per possible value
  Counting lets us instantly see which number has count 2 (duplicate) and
  which has count 0 (missing). This counting pattern is one of the most
  important tricks in all of DSA -- learn it well here.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    2 <= nums.length <= 10000   -> at least 2 numbers
    1 <= nums[i] <= 10000       -> values are between 1 and n
  Exactly one duplicate and exactly one missing -- guaranteed by the problem.


EDGE CASES (unusual inputs to check)
------------------------------------
- Smallest: [1, 1] -> duplicate 1, missing 2 -> [1, 2]
- Missing the first number: [2, 2] -> [2, 1]
- Missing the last number:  [1, 1] -> [1, 2]   (same as above pattern)
- Duplicate at the end:     [3, 2, 3] (n=3) -> [3, 1]


SPEED & MEMORY (time / space complexity)
----------------------------------------
We will show three approaches with different trade-offs:
  - Counting (Solution 1): Time O(n), Space O(n)  -- easiest to understand.
  - Math    (Solution 2): Time O(n), Space O(1)   -- clever, tiny memory.
  - In-place mark (Sol 3): Time O(n), Space O(1)  -- advanced index trick.
"O(n)" = work/memory grows in a straight line with input size.
"O(1)" = uses a fixed, tiny amount of extra memory no matter how big n is.
"""

from typing import List
from collections import Counter   # a ready-made counting tool (explained below)


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: count how many times each number appears  (EASIEST)
    # ----------------------------------------------------------------
    #
    # Plan:
    #   1) Tally every number: how many times did each value appear?
    #   2) The value with tally 2 is the DUPLICATE.
    #   3) The value in 1..n with tally 0 is the MISSING one.
    #
    # `Counter(nums)` walks the list and builds those tallies for us.
    #   Counter([1,2,2,4]) -> {1:1, 2:2, 4:1}   (value -> count)
    #
    # Time: O(n)   Space: O(n)  (we store a tally for up to n different values)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)                 # the numbers should be 1..n
        counts = Counter(nums)        # value -> how many times it appears

        duplicate = -1                # we'll fill these in; -1 = "not found yet"
        missing = -1

        # Check every number that SHOULD exist: 1, 2, ..., n.
        # range(1, n + 1) gives 1..n  (the +1 is because range stops one early).
        for value in range(1, n + 1):
            c = counts.get(value, 0)  # .get(value, 0) = its count, or 0 if absent
            if c == 2:
                duplicate = value     # appears twice -> the duplicate
            elif c == 0:
                missing = value       # appears zero times -> the missing one

        return [duplicate, missing]

    # ----------------------------------------------------------------
    # SOLUTION 1b: same idea but with a plain counting ARRAY (no Counter)
    # ----------------------------------------------------------------
    #
    # Instead of Counter, make our own tally row of size n+1 (indexes 0..n).
    # We ignore index 0 and use indexes 1..n to match the values 1..n.
    # seen[v] will hold "how many times value v appeared."
    #
    # This shows what Counter does "under the hood" -- it's just tallies.
    #
    # Time: O(n)   Space: O(n)
    def findErrorNums_array(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [0] * (n + 1)          # n+1 slots so index n is valid; slot 0 unused
        for num in nums:
            seen[num] += 1            # add one to that value's tally

        duplicate = -1
        missing = -1
        for value in range(1, n + 1):
            if seen[value] == 2:
                duplicate = value
            elif seen[value] == 0:
                missing = value
        return [duplicate, missing]

    # ----------------------------------------------------------------
    # SOLUTION 2: MATH with sums  (O(1) extra space, very clever)
    # ----------------------------------------------------------------
    #
    # Two facts we can compute:
    #   - The CORRECT numbers 1..n add up to a known total.
    #     Formula: 1 + 2 + ... + n = n * (n + 1) / 2.  (a famous shortcut)
    #   - The CORRECT numbers, with NO repeats, are the unique values present.
    #
    # Let:
    #   actual_sum        = sum of the broken list (has the dup, missing one gone)
    #   actual_sum_unique = sum of the DISTINCT values present (dup counted once)
    #   expected_sum      = sum of 1..n (what it should be)
    #
    # Then:
    #   duplicate = actual_sum - actual_sum_unique
    #       (the extra copy is the only difference between counting the dup
    #        twice vs once)
    #   missing   = expected_sum - actual_sum_unique
    #       (what's left over after removing every value that IS present)
    #
    # `set(nums)` keeps only the DISTINCT values (drops repeats):
    #   set([1,2,2,4]) -> {1, 2, 4}
    #
    # Time: O(n)   Space: O(1) extra  (set is O(n) though; see note)
    # NOTE: building set(nums) technically uses O(n) memory. A truly O(1)-space
    # version uses sum-of-squares; shown as Solution 2b for completeness.
    def findErrorNums_math(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2     # // is integer division (no decimals)
        actual_sum = sum(nums)              # sum() adds up every item in the list
        actual_sum_unique = sum(set(nums))  # sum of distinct values

        duplicate = actual_sum - actual_sum_unique
        missing = expected_sum - actual_sum_unique
        return [duplicate, missing]

    # ----------------------------------------------------------------
    # SOLUTION 2b: pure math, true O(1) space  (sum + sum of squares)
    # ----------------------------------------------------------------
    #
    # Let d = duplicate, m = missing. Compare the broken list to the perfect one:
    #   (sum of nums) - (sum of 1..n)            =  d - m
    #   (sum of nums^2) - (sum of 1..n squared)  =  d^2 - m^2  = (d - m)(d + m)
    # From the first line we know (d - m). Divide the second by (d - m) to get
    # (d + m). Now we have d - m and d + m, so:
    #   d = ((d+m) + (d-m)) / 2 ,  m = ((d+m) - (d-m)) / 2
    #
    # No set, no Counter -> only a few number variables -> O(1) space.
    # Heavier on math; know it exists, but Solution 1 is fine to SAY in an
    # interview unless they ask for O(1) space.
    #
    # Time: O(n)   Space: O(1)
    def findErrorNums_math2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # sum of 1..n  and  sum of 1^2..n^2 (the second has its own formula)
        expected_sum = n * (n + 1) // 2
        expected_sq = n * (n + 1) * (2 * n + 1) // 6

        actual_sum = sum(nums)
        actual_sq = sum(x * x for x in nums)

        diff = actual_sum - expected_sum          # = d - m
        sq_diff = actual_sq - expected_sq         # = d^2 - m^2 = (d-m)(d+m)
        sum_dm = sq_diff // diff                  # = d + m

        duplicate = (sum_dm + diff) // 2          # d
        missing = (sum_dm - diff) // 2            # m
        return [duplicate, missing]

    # ----------------------------------------------------------------
    # SOLUTION 3: in-place negative marking  (ADVANCED index trick)
    # ----------------------------------------------------------------
    #
    # Idea: use the list ITSELF as the tally sheet, so we need no extra memory.
    # The values are 1..n, which double as INDEXES into the same list.
    #
    # For each number v we see, go to slot (v-1) and make the number there
    # NEGATIVE -- that's our "I have visited this value" mark. If we arrive at
    # a slot that is ALREADY negative, it means this value was seen before ->
    # it's the DUPLICATE. After marking, the one slot still POSITIVE is the
    # value that was never visited -> the MISSING one.
    #
    # We use abs(v) (absolute value = drop the minus sign) when reading a value,
    # because earlier marking may have flipped its sign.
    #
    # This mutates the input. It's a famous interview trick for O(1) space;
    # understand it, but only reach for it if asked to avoid extra memory.
    #
    # Time: O(n)   Space: O(1)
    def findErrorNums_mark(self, nums: List[int]) -> List[int]:
        duplicate = -1
        for num in nums:
            idx = abs(num) - 1            # value v lives at slot v-1
            if nums[idx] < 0:            # already marked -> seen before
                duplicate = abs(num)
            else:
                nums[idx] = -nums[idx]    # mark as visited by flipping sign

        # The slot still positive points to the missing value.
        missing = -1
        for i in range(len(nums)):
            if nums[i] > 0:
                missing = i + 1           # slot i corresponds to value i+1
                break
        return [duplicate, missing]


# =====================================================================
# LOCAL TESTING
# =====================================================================
if __name__ == "__main__":
    s = Solution()

    # Each entry: (input list, expected [duplicate, missing])
    tests = [
        ([1, 2, 2, 4], [2, 3]),
        ([1, 1],       [1, 2]),     # edge: smallest list
        ([2, 2],       [2, 1]),     # edge: missing the first number
        ([3, 2, 3],    [3, 1]),     # edge: duplicate at the end, missing 1
        ([1, 2, 4, 4], [4, 3]),
    ]

    # Methods that DO NOT modify the input (safe to reuse the same list):
    non_mutating = [
        s.findErrorNums,
        s.findErrorNums_array,
        s.findErrorNums_math,
        s.findErrorNums_math2,
    ]
    for nums, expected in tests:
        for m in non_mutating:
            assert m(list(nums)) == expected, f"{m.__name__} failed on {nums}"

    # Solution 3 mutates its input, so give each call a FRESH copy:
    for nums, expected in tests:
        assert s.findErrorNums_mark(list(nums)) == expected, \
            f"findErrorNums_mark failed on {nums}"

    print("all tests pass")
