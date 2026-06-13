r"""
=====================================================================
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
For EACH number in the list, count how many OTHER numbers are smaller than it.
Build a new list of those counts, in the same order.

    nums = [8, 1, 2, 2, 3]
    For 8 -> smaller ones are 1,2,2,3        -> 4
    For 1 -> nothing is smaller              -> 0
    For 2 -> only 1 is smaller               -> 1
    For 2 -> only 1 is smaller               -> 1
    For 3 -> 1,2,2 are smaller               -> 3
    answer = [4, 0, 1, 1, 3]

"Smaller" means strictly less than (<). Equal numbers do NOT count.
Notice [2 and 2]: each is NOT smaller than the other, so equals are ignored.


WORDS / IDEAS YOU NEED
----------------------
- We compare every value against the others and TALLY the smaller ones.
- BRUTE FORCE: the obvious "check everything against everything" way.
  Simple but slow. Good first answer, then we improve it.
- COUNTING + PREFIX SUM (the clever upgrade):
  Because values are small (0..100 here), we can COUNT how many of each value
  exist, then use a "running total" so that for any value v we instantly know
  "how many numbers are smaller than v" without re-scanning the list.

- PREFIX SUM (new big idea):
  A prefix sum is a RUNNING TOTAL as you move along.
  If counts = how many of each value, then the prefix sum up to (v-1) =
  "how many numbers are <= v-1" = "how many numbers are strictly smaller than v."
  Building running totals once lets us answer each question in one lookup.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    2 <= nums.length <= 500
    0 <= nums[i] <= 100     -> values are SMALL (only 0..100). This is the key
                               that makes the counting approach possible:
                               we can keep a tally slot for each of 101 values.


EDGE CASES (unusual inputs to check)
------------------------------------
- All equal:   [7,7,7,7] -> [0,0,0,0]  (nothing is smaller than anything)
- Already sorted up: [6,5,4,8] handled fine regardless of order
- Value 0 present: 0 can never have anything smaller -> its count is 0
- Duplicates: equal values get the SAME count (see the two 2s above)


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Solution 1 (brute force): Time O(n^2), Space O(n).
    For each of n numbers we scan all n numbers -> n*n comparisons.
- Solution 2 (counting + prefix sum): Time O(n + k), Space O(k + n).
    k = the value range (here 101). We pass the list a couple of times and
    the buckets a fixed number of times -> much faster for big n.
    This is the OPTIMAL, interview-preferred answer here.
- Solution 3 (sort + lookup): Time O(n log n), Space O(n).
    Sorting groups equal values; an index map gives each value its count.
"O(n^2)" = work grows with the SQUARE of input (slow). "O(n+k)" = grows in a
straight line with input size + value range (fast).
"""

from typing import List


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: brute force -- compare each number to all the others
    # ----------------------------------------------------------------
    #
    # The literal reading of the problem: for each i, walk the whole list and
    # count how many values are strictly less than nums[i].
    #
    # Easy to write and explain. Slow for large n because it does n*n work.
    # Perfectly fine to STATE first in an interview, then say "I can do better."
    #
    # Time: O(n^2)   Space: O(n)  (the answer list)
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):          # for each position i
            count = 0
            for j in range(len(nums)):      # compare against every position j
                if nums[j] < nums[i]:       # strictly smaller? tally it
                    count += 1
                # note: when j == i, nums[j] < nums[i] is False, so no need to
                # skip it explicitly -- a number is never smaller than itself.
            ans.append(count)
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 2: counting + prefix sum  (OPTIMAL -- learn this well)
    # ----------------------------------------------------------------
    #
    # Big idea in 3 steps:
    #   STEP A -- COUNT: how many of each value 0..100 are there?
    #       counts[v] = how many times value v appears.
    #   STEP B -- PREFIX SUM: turn counts into "how many are <= v".
    #       prefix[v] = counts[0] + counts[1] + ... + counts[v].
    #       Then "how many are STRICTLY smaller than v" = prefix[v-1]
    #       (everything up to v-1). For v == 0 that's 0.
    #   STEP C -- ANSWER: for each original number, look up that running total.
    #
    # Why it's fast: we never compare numbers against each other. We build the
    # tallies once, then every answer is a single instant lookup.
    #
    # Time: O(n + k)   Space: O(k + n)   (k = 101 possible values)
    def smallerNumbersThanCurrent_count(self, nums: List[int]) -> List[int]:
        MAX_VAL = 100                          # given: values are 0..100
        counts = [0] * (MAX_VAL + 1)           # 101 tally slots, all start at 0

        # STEP A: count each value
        for num in nums:
            counts[num] += 1

        # STEP B: turn counts into a running total (prefix sum).
        # After this loop, prefix[v] = how many numbers are <= v.
        prefix = [0] * (MAX_VAL + 1)
        running = 0
        for v in range(MAX_VAL + 1):
            prefix[v] = running        # numbers strictly less than v = total so far
            running += counts[v]       # now fold v's own count into the running total
        # Trick: by storing the running total BEFORE adding counts[v], prefix[v]
        # already means "how many are strictly smaller than v". Neat and exact.

        # STEP C: each number's answer is prefix[that number]
        return [prefix[num] for num in nums]

    # ----------------------------------------------------------------
    # SOLUTION 3: sort + first-index map
    # ----------------------------------------------------------------
    #
    # Idea: if we SORT the values, then for any value its count of smaller
    # numbers equals the INDEX where it first appears in the sorted list.
    #
    #   nums        = [8, 1, 2, 2, 3]
    #   sorted_nums = [1, 2, 2, 3, 8]
    #                  0  1     3  4   <- first index of each distinct value
    #   value 1 first appears at index 0 -> 0 smaller
    #   value 2 first appears at index 1 -> 1 smaller
    #   value 3 first appears at index 3 -> 3 smaller
    #   value 8 first appears at index 4 -> 4 smaller
    #
    # We record each value's FIRST index in a dictionary, then look up each
    # original number. Using "if value not in first_index" keeps only the
    # FIRST (smallest index) for duplicates, which is exactly what we want.
    #
    # Time: O(n log n)  (the sort dominates)   Space: O(n)
    def smallerNumbersThanCurrent_sort(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)             # sorted() returns a new sorted list
        first_index = {}                       # value -> index of its first appearance
        for i, value in enumerate(sorted_nums):
            # enumerate gives (index, value) pairs: (0,1),(1,2),(2,2),(3,3),(4,8)
            if value not in first_index:       # keep only the earliest index
                first_index[value] = i
        return [first_index[num] for num in nums]


# =====================================================================
# LOCAL TESTING
# =====================================================================
if __name__ == "__main__":
    s = Solution()

    # Each entry: (input list, expected answer list)
    tests = [
        ([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
        ([6, 5, 4, 8],    [2, 1, 0, 3]),
        ([7, 7, 7, 7],    [0, 0, 0, 0]),   # edge: all equal -> all zeros
        ([0, 1],          [0, 1]),         # edge: contains value 0
        ([2, 2],          [0, 0]),         # edge: duplicates, none smaller
    ]

    methods = [
        s.smallerNumbersThanCurrent,
        s.smallerNumbersThanCurrent_count,
        s.smallerNumbersThanCurrent_sort,
    ]

    for nums, expected in tests:
        for m in methods:
            assert m(list(nums)) == expected, f"{m.__name__} failed on {nums}"

    print("all tests pass")
