"""
=====================================================================
1929. Concatenation of Array
https://leetcode.com/problems/concatenation-of-array/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
You are given a row of numbers. Call this row `nums`.
You must make a NEW row that is the same numbers written twice, back to back.

    nums = [1, 2, 1]
    answer = [1, 2, 1,  1, 2, 1]
                ^first copy   ^second copy

That's it. "Concatenation" is a fancy word for "stick two things together
end to end."


SOME WORDS YOU NEED TO KNOW FIRST
---------------------------------
- ARRAY / LIST:
  A "list" in Python is just an ordered row of items, written with square
  brackets:  [1, 2, 1]. LeetCode calls it an "array" (other languages use
  that word), but in Python the tool we use is called a `list`.
  Why use a list? Because we need to keep many numbers together in ORDER,
  and we need to know "what is the 1st number, the 2nd number," etc.

- INDEX:
  The POSITION of an item in the list. Python starts counting at 0, not 1.
  For nums = [1, 2, 1]:
        index:   0  1  2
        value:   1  2  1
  So nums[0] is 1, nums[1] is 2, nums[2] is 1.
  We say "nums[i]" to mean "the item at position i."

- n  (the length):
  `n` is just a name for "how many numbers are in the list."
  For [1, 2, 1], n = 3. The final answer has length 2*n (here, 6).

- WHY IS IT CALLED `nums`?
  It is just a NAME (a variable). LeetCode chose the name `nums` (short for
  "numbers"). We could call it anything, but we keep the given name so our
  code matches the problem.


THE GOAL, written exactly:
    answer[i]     should equal nums[i]      for every position 0..n-1
    answer[i + n] should equal nums[i]      for every position 0..n-1
The first line fills the FIRST copy, the second line fills the SECOND copy.


CONSTRAINTS (the rules the input always follows)
------------------------------------------------
    n == len(nums)         -> n is the length of nums
    1 <= n <= 1000         -> the list is never empty (at least 1 number)
    1 <= nums[i] <= 1000   -> the actual values don't matter to our logic;
                              this is purely about POSITIONS, not values.


EDGE CASES (unusual inputs to make sure we don't break on)
----------------------------------------------------------
- Smallest list: n == 1, e.g. [5] -> [5, 5].
- Repeated numbers, e.g. [7, 7] -> [7, 7, 7, 7]. Works fine because we
  copy by POSITION, we never care if two values are the same.


HOW FAST / HOW MUCH MEMORY  (time & space complexity)
-----------------------------------------------------
- The answer itself has 2*n items, so we MUST write 2*n items no matter what.
- "Time complexity O(n)" means: the work grows in a straight line with n.
  Twice the input -> twice the work. This is the best possible here, because
  we are forced to produce 2*n items.
- "Space complexity O(n)" means: the extra memory we use also grows in a
  straight line with n (the answer list takes 2*n slots).
- O(n) is read as "order n." Don't overthink it: it just describes how the
  cost scales as the input gets bigger.
"""

# `from typing import List` brings in a helper called `List` so we can WRITE
# DOWN what type of value goes in and comes out of our function.
# This is called a "type hint." It does NOT change how the code runs --
# it is a note for humans (and tools) saying "this is a list of integers."
from typing import List


# `class Solution:` groups our functions together.
# LeetCode requires this exact name `Solution`. Think of a class as a folder
# that holds related functions. You don't need to fully understand classes
# yet -- just know LeetCode looks for `Solution` and the method inside it.
class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: the simple, recommended answer  (say THIS in an interview)
    # ----------------------------------------------------------------
    #
    # Reading the function header piece by piece:
    #   def              -> "define a function" (a reusable block of steps)
    #   getConcatenation -> the function's name (LeetCode gives us this name)
    #   self             -> always the first word inside a class method;
    #                       ignore it for now, it just means "this object"
    #   nums: List[int]  -> the input. Name is `nums`, and `: List[int]`
    #                       is the type hint = "a list of integers"
    #   -> List[int]     -> what we GIVE BACK: also a list of integers
    #
    # The actual idea:
    #   In Python, the `+` sign between two lists glues them together.
    #   [1,2] + [3,4]  becomes  [1,2,3,4].
    #   So `nums + nums` glues nums to a second copy of itself = the answer.
    #
    # Time:  O(n)  (we copy 2*n numbers)
    # Space: O(n)  (the new list holds 2*n numbers)
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums   # glue nums to itself -> first copy then second copy

    # ----------------------------------------------------------------
    # SOLUTION 2: multiply a list  (a Python shortcut, same result)
    # ----------------------------------------------------------------
    #
    # In Python, multiplying a list by a number REPEATS it.
    #   [1,2] * 3  becomes  [1,2,1,2,1,2]
    # So `nums * 2` means "this list, repeated 2 times" = nums then nums.
    # Same speed and memory as Solution 1, just shorter to type.
    #
    # Time:  O(n)   Space: O(n)
    def getConcatenation_mul(self, nums: List[int]) -> List[int]:
        return nums * 2

    # ----------------------------------------------------------------
    # SOLUTION 3: build it by hand, position by position
    # ----------------------------------------------------------------
    #
    # This one does NOT use the `+` shortcut. Instead it literally follows
    # the problem's rule: answer[i] = nums[i] and answer[i+n] = nums[i].
    # Good to understand because in many other languages you can't just
    # use `+`, you have to fill positions one by one like this.
    #
    # Time:  O(n)   Space: O(n)
    def getConcatenation_index(self, nums: List[int]) -> List[int]:
        # `len(nums)` counts how many items are in nums. Store it in `n`
        # so we don't have to recount it every time we need it.
        n = len(nums)

        # `[0] * (2 * n)` makes a list of 2*n zeros, e.g. [0,0,0,0,0,0].
        # We create the answer at FULL SIZE up front, filled with placeholder
        # zeros, then we will overwrite each slot with the real number.
        # Why pre-make it? So we can put numbers directly at any position.
        ans = [0] * (2 * n)

        # `range(n)` produces the positions 0, 1, 2, ..., n-1, one at a time.
        # `for i in range(n):` runs the indented block once for each position.
        for i in range(n):
            ans[i] = nums[i]        # fill the FIRST copy:  slot i        = nums[i]
            ans[i + n] = nums[i]    # fill the SECOND copy: slot i + n    = nums[i]
        # After the loop, every one of the 2*n slots holds the right number.
        return ans

    # ----------------------------------------------------------------
    # SOLUTION 4: start empty and add the numbers
    # ----------------------------------------------------------------
    #
    # `[]` is an empty list (a row with nothing in it yet).
    # `.extend(other_list)` takes every item from `other_list` and adds them
    # to the end of our list, one after another.
    # So we extend with nums (first copy), then extend with nums again
    # (second copy).
    #
    # Time:  O(n)   Space: O(n)
    def getConcatenation_extend(self, nums: List[int]) -> List[int]:
        ans = []            # start with an empty list
        ans.extend(nums)    # add all of nums -> this is the first copy
        ans.extend(nums)    # add all of nums again -> the second copy
        return ans


# =====================================================================
# TESTING OUR CODE
# =====================================================================
# Everything under `if __name__ == "__main__":` runs ONLY when you execute
# this file directly (python 1929_concatenation_of_array.py). It is our
# little self-check so we KNOW the solutions are correct.
if __name__ == "__main__":

    # `s = Solution()` creates one copy of our Solution "folder" so we can
    # call the functions inside it as  s.getConcatenation(...).
    s = Solution()

    # Each pair below is (input we give, output we expect to get back).
    tests = [
        ([1, 2, 1],    [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([5],          [5, 5]),            # edge case: only one number
        ([7, 7],       [7, 7, 7, 7]),      # edge case: repeated numbers
    ]

    # A list of all four solution functions so we can test them all at once.
    methods = [
        s.getConcatenation,
        s.getConcatenation_mul,
        s.getConcatenation_index,
        s.getConcatenation_extend,
    ]

    # For every test, run every method and check the result matches.
    for nums, expected in tests:
        for m in methods:
            # `assert X` means "X had better be True; if not, stop and shout."
            # We pass list(nums) (a fresh copy) so one method can't disturb
            # the input for the next method.
            assert m(list(nums)) == expected, f"{m.__name__} failed on {nums}"

    # If we reach here, nothing failed.
    print("all tests pass")
