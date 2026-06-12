"""
=====================================================================
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
You get a list made of only 0s and 1s (a "binary array").
Find the LONGEST unbroken run of 1s, and return how long that run is.

    nums = [1, 1, 0, 1, 1, 1]
           \--/      \------/
           run=2      run=3      -> answer is 3 (the longest run)

A "0" breaks the streak. When you hit a 0, the current run of 1s ends.


THE KEY IDEA (how a human would do it by eye)
---------------------------------------------
Walk left to right keeping TWO counters:
  - `current`: how many 1s in a row RIGHT NOW (the streak you are on)
  - `best`:    the biggest streak you have seen SO FAR

Rules while walking:
  - see a 1  -> streak grows:   current = current + 1
  - see a 0  -> streak breaks:  current = 0   (start counting again from scratch)
  - after each step, remember the best:  best = max(best, current)

That's the whole trick: a counter that grows on 1, resets on 0, and a
"high score" that only ever goes up.


WORDS / IDEAS YOU NEED
----------------------
- BINARY ARRAY: a list whose items are only 0 or 1. Nothing fancy --
  "binary" just means "two possible values."
- CONSECUTIVE: next to each other with no gap. [1,1,1] is 3 consecutive 1s.
  [1,0,1] is NOT -- the 0 splits them, so the best run there is 1.
- RUNNING COUNTER: a number we keep updating as we move through the list,
  instead of recomputing everything from the start each time.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    1 <= nums.length <= 100000   -> list is never empty; can be large, so we
                                    want a fast single pass (O(n)).
    nums[i] is 0 or 1            -> only two possible values, ever.


EDGE CASES (unusual inputs to check)
------------------------------------
- All ones:   [1,1,1] -> 3   (streak never breaks)
- All zeros:  [0,0,0] -> 0   (there is no run of 1s at all)
- Single item:[1] -> 1 ,  [0] -> 0
- Ends with the longest run, e.g. [0,1,1] -> 2  (must not "forget" the last
  streak just because the list ended -- our running max already handles this)


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Time  O(n): we look at each number exactly once (one pass left to right).
              n can be up to 100000, so one pass is the right speed.
- Space O(1): we only keep two small counters, no matter how big the list is.
              ("O(1)" = constant extra memory; it does NOT grow with input.)
              This is the big difference from the earlier problems, where we
              had to BUILD a new list (O(n) space). Here we just return a
              single number, so we need almost no extra memory.
"""

from typing import List   # type hint helper: "List[int]" means a list of ints


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: one pass with two counters  (THE answer -- learn this)
    # ----------------------------------------------------------------
    #
    # Reading the header:
    #   nums: List[int]  -> input list of 0s and 1s
    #   -> int           -> we return a single whole number (the longest run)
    #
    # Time: O(n)   Space: O(1)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0       # longest streak seen so far (our "high score")
        current = 0    # length of the streak we are currently on

        for num in nums:        # `num` is each value in the list, one at a time
            if num == 1:
                current += 1                  # streak continues -> grow it
                # `max(a, b)` gives the LARGER of two numbers.
                # If this new streak beat the record, update the record.
                best = max(best, current)
            else:               # num is 0
                current = 0                   # streak broke -> reset to zero

        return best

    # ----------------------------------------------------------------
    # SOLUTION 2: same logic, update best AFTER the if/else (cleaner shape)
    # ----------------------------------------------------------------
    #
    # Exactly the same idea, but we compute `current` first, then take the max
    # once per step. Some people find this layout easier to read.
    # Note: when num is 0, current becomes 0, and max(best, 0) leaves best
    # unchanged -- so it's still correct.
    #
    # Time: O(n)   Space: O(1)
    def findMaxConsecutiveOnes_v2(self, nums: List[int]) -> int:
        best = 0
        current = 0
        for num in nums:
            current = current + 1 if num == 1 else 0   # grow on 1, reset on 0
            best = max(best, current)
        return best

    # ----------------------------------------------------------------
    # SOLUTION 3: Pythonic trick -- split on zeros, measure the pieces
    # ----------------------------------------------------------------
    #
    # Idea: turn the list into a string of characters, then SPLIT it wherever
    # there is a 0. Each leftover piece is a block of 1s; the longest piece's
    # length is our answer.
    #
    # Step by step for [1,1,0,1,1,1]:
    #   1) "".join(...)  glues the digits into the text  "110111"
    #   2) .split("0")   cuts at every 0  ->  ["11", "", "111"]
    #   3) max(..., key=len) picks the longest piece -> "111"
    #   4) len(...) -> 3
    #
    # Clever and short, but it builds a string (O(n) extra space) and is
    # harder to reason about. Good to KNOW, but Solution 1 is the interview
    # answer because it's O(1) space and clearer.
    #
    # Time: O(n)   Space: O(n)  (because of the temporary string/pieces)
    def findMaxConsecutiveOnes_split(self, nums: List[int]) -> int:
        text = "".join(str(num) for num in nums)   # e.g. "110111"
        pieces = text.split("0")                    # e.g. ["11", "", "111"]
        # max(..., key=len) compares pieces by their length and returns the
        # longest one; len() then gives its length. `default=""` guards the
        # case where pieces is empty (can't happen here, but safe habit).
        return len(max(pieces, key=len, default=""))


# =====================================================================
# LOCAL TESTING
# =====================================================================
# Runs only when you execute this file directly (python <file>.py).
# LeetCode ignores this and calls findMaxConsecutiveOnes itself.
if __name__ == "__main__":
    s = Solution()

    # Each entry: (input list, expected longest run)
    tests = [
        ([1, 1, 0, 1, 1, 1], 3),
        ([1, 0, 1, 1, 0, 1], 2),
        ([1, 1, 1],          3),   # edge: all ones
        ([0, 0, 0],          0),   # edge: all zeros (no run of 1s)
        ([1],                1),   # edge: single 1
        ([0],                0),   # edge: single 0
        ([0, 1, 1],          2),   # edge: longest run is at the very end
    ]

    methods = [
        s.findMaxConsecutiveOnes,
        s.findMaxConsecutiveOnes_v2,
        s.findMaxConsecutiveOnes_split,
    ]

    for nums, expected in tests:
        for m in methods:
            assert m(list(nums)) == expected, f"{m.__name__} failed on {nums}"

    print("all tests pass")
