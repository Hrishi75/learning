r"""
=====================================================================
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
You get a list of n numbers. Every number is somewhere in the range 1..n.
But some numbers in 1..n might be missing (and others appear more than once).
Return ALL the numbers from 1..n that DO NOT appear in the list.

    nums = [4, 3, 2, 7, 8, 2, 3, 1]    (n = 8, so we expect 1..8)
    present: 1,2,3,4,7,8     missing: 5,6
    answer = [5, 6]

This is like problem 645 (Set Mismatch), but here MANY numbers can be missing
and many can repeat -- we must list every missing one.


WORDS / IDEAS YOU NEED
----------------------
- n: the list length. The "complete" set we compare against is 1..n.
- We want the numbers in 1..n that are absent.
- TWO mental tools we already know reappear here:
    * counting / membership:  mark which numbers we have seen.
    * in-place negative marking: use the list itself as the "seen" sheet so we
      use no extra memory (this is the follow-up's O(1)-space answer).


THE FOLLOW-UP (the real challenge)
----------------------------------
"Could you do it WITHOUT extra space and in O(n) time? The returned list does
 not count as extra space."
=> They want O(n) time AND O(1) extra memory. A set or counting array uses
   O(n) extra memory, so it does NOT satisfy the follow-up. The negative-
   marking trick (Solution 3) DOES -- it is the intended answer.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    n == nums.length
    1 <= n <= 100000        -> can be large; we want O(n) time
    1 <= nums[i] <= n       -> every value is a valid index target (1..n).
                               This is the magic that enables marking: each
                               value can point at a slot inside the same list.


EDGE CASES (unusual inputs to check)
------------------------------------
- Nothing missing: [1,2,3] -> []   (every number present -> empty answer)
- All the same:    [1,1]   -> [2]  (1 present, 2 missing)
- All identical large dup: [2,2] -> [1]
- Single element:  [1]     -> []   (1..1 all present)


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Solution 1 (set):            Time O(n), Space O(n)   -- easiest.
- Solution 2 (counting array): Time O(n), Space O(n)   -- same idea, raw tally.
- Solution 3 (negative mark):  Time O(n), Space O(1)   -- the FOLLOW-UP answer.
- Solution 4 (cyclic sort):    Time O(n), Space O(1)   -- put each value home.
(The returned answer list is not counted as "extra space" per the problem.)
"""

from typing import List


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: use a set of what we've seen  (EASIEST -- say this first)
    # ----------------------------------------------------------------
    #
    # A "set" stores unique values and answers "is x in here?" instantly.
    # Steps:
    #   1) put every number we have into a set (so duplicates collapse).
    #   2) walk 1..n; any value NOT in the set is missing -> collect it.
    #
    # `set(nums)` builds that membership set in one shot.
    # `value not in seen` is the instant "is it absent?" check.
    #
    # Time: O(n)   Space: O(n)  (the set) -- does NOT meet the follow-up.
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set(nums)                 # unique values that are present
        ans = []
        for value in range(1, n + 1):    # check every number that SHOULD exist
            if value not in seen:
                ans.append(value)
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 2: counting array  (same idea, shows the tally explicitly)
    # ----------------------------------------------------------------
    #
    # Instead of a set, keep a row of tallies of size n+1 (indexes 0..n).
    # present[v] becomes True/1 when we have seen value v. Then any v in 1..n
    # whose slot is still 0 was never seen -> missing.
    #
    # Time: O(n)   Space: O(n)  -- still doesn't meet the follow-up.
    def findDisappearedNumbers_count(self, nums: List[int]) -> List[int]:
        n = len(nums)
        present = [False] * (n + 1)      # slot 0 unused; slots 1..n track values
        for num in nums:
            present[num] = True          # mark this value as seen
        return [v for v in range(1, n + 1) if not present[v]]

    # ----------------------------------------------------------------
    # SOLUTION 3: in-place negative marking  (THE FOLLOW-UP ANSWER)
    # ----------------------------------------------------------------
    #
    # Goal: O(n) time, O(1) extra space. Trick: the values are 1..n, so each
    # value can point at a SLOT in the same list. We mark "value v was seen"
    # by making the number at slot (v-1) NEGATIVE. Negative = "this position's
    # value showed up." We never lose information because we only flip the
    # SIGN; the size of the number stays the same, and we read it with abs().
    #
    # PASS 1 -- mark:
    #   for each number, compute its home slot index = abs(num) - 1,
    #   and flip the sign of nums[index] to negative (if not already).
    #
    # PASS 2 -- read:
    #   any slot i that is still POSITIVE means value (i+1) was never marked,
    #   i.e. (i+1) is missing. Collect those.
    #
    # abs(num) = drop the minus sign, because earlier marking may have turned
    # this very number negative; we still need its original magnitude.
    #
    # Time: O(n)   Space: O(1) extra  (we reuse the input list; answer excluded)
    # NOTE: this MUTATES the input list.
    def findDisappearedNumbers_mark(self, nums: List[int]) -> List[int]:
        # PASS 1: mark seen values by flipping signs
        for num in nums:
            index = abs(num) - 1             # value v -> slot v-1
            if nums[index] > 0:              # not yet marked
                nums[index] = -nums[index]   # mark as seen (make negative)

        # PASS 2: positive slots reveal the missing values
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:                  # value (i+1) was never marked
                ans.append(i + 1)
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 4: cyclic sort  (alternative O(1)-space idea -- good to know)
    # ----------------------------------------------------------------
    #
    # Idea: try to put every value into its "home" position, where value v
    # belongs at index v-1. Walk the list; if the current value is not already
    # home AND its home doesn't already hold the right value, SWAP it home.
    # After this shuffling, scan: any index i whose value isn't (i+1) means
    # (i+1) is missing.
    #
    # This does NOT destroy the values (unlike marking, which flips signs);
    # it rearranges them. Slightly trickier loop, but a classic pattern for
    # "numbers in range 1..n" problems.
    #
    # Time: O(n)   (each value is moved home at most once)   Space: O(1)
    # NOTE: this MUTATES (reorders) the input list.
    def findDisappearedNumbers_cyclic(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            home = nums[i] - 1               # where nums[i] should live
            if nums[i] != nums[home]:        # home doesn't already hold this value
                nums[i], nums[home] = nums[home], nums[i]   # swap it home
                # do NOT advance i: the value we just swapped IN also needs placing
            else:
                i += 1                       # already correct (or a dup) -> move on
        # Now any spot not holding its proper value points to a missing number.
        return [idx + 1 for idx in range(n) if nums[idx] != idx + 1]


# =====================================================================
# LOCAL TESTING
# =====================================================================
if __name__ == "__main__":
    s = Solution()

    # Each entry: (input list, expected list of missing numbers)
    tests = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1],                   [2]),
        ([1, 2, 3],                []),     # edge: nothing missing
        ([2, 2],                   [1]),    # edge: 1 missing
        ([1],                      []),     # edge: single element, present
        ([2, 2, 2, 2],             [1, 3, 4]),
    ]

    # Methods that MUTATE the input each need a fresh copy per call.
    methods = [
        s.findDisappearedNumbers,
        s.findDisappearedNumbers_count,
        s.findDisappearedNumbers_mark,
        s.findDisappearedNumbers_cyclic,
    ]

    for nums, expected in tests:
        for m in methods:
            assert m(list(nums)) == expected, f"{m.__name__} failed on {nums}"

    print("all tests pass")
