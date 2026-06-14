r"""
=====================================================================
1441. Build an Array With Stack Operations
https://leetcode.com/problems/build-an-array-with-stack-operations/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
A stream spits out the numbers 1, 2, 3, ..., n in order.
You have a stack (a pile where you add/remove only from the TOP).
Two moves: "Push" (read next stream number, put on top) and "Pop" (throw away
the top). Using these moves, make the stack (bottom -> top) exactly equal
`target`. Return the LIST OF MOVES you used.

    target = [1, 3],  n = 3
    stream gives 1,2,3 in order.
      read 1 -> we WANT 1 -> "Push"            stack: [1]
      read 2 -> we DON'T want 2 -> "Push" then "Pop"  stack: [1]
      read 3 -> we WANT 3 -> "Push"            stack: [1,3]  == target, STOP
    answer = ["Push","Push","Pop","Push"]

Key rule from the problem: EVERY number you take from the stream must be Pushed
first. If you don't actually want it, you immediately Pop it back off. And once
the stack equals target, you STOP -- no extra reads, no extra moves.


THE KEY IDEA (this is a SIMULATION problem)
-------------------------------------------
"Simulation" = just DO what the story says, step by step, and record the moves.
No fancy math. Walk the stream number by number and decide:

    current stream number == the target value we still need ?
        YES -> "Push"  (keep it; move on to the next target value)
        NO  -> "Push","Pop"  (we were forced to read it, so push then drop it)

We only care about stream numbers up to the LARGEST value in target. Anything
after the last target value is never needed -> we stop early.

Because target is strictly increasing (each value bigger than the last) and all
values are within 1..n, we can simply walk a counter through the stream and a
pointer through target.


WORDS / IDEAS YOU NEED
----------------------
- STACK: a pile with LIFO order = "Last In, First Out." You can only touch the
  TOP. Push = add on top. Pop = remove from top. Think of a stack of plates.
  (We don't even need to build a real stack here -- we only need the MOVES.
   But understanding the stack is what makes the moves make sense.)
- STREAM: numbers arriving one at a time in fixed order 1,2,...,n. You can't
  skip ahead; to reach 3 you must first read 1 and 2.
- SIMULATION: model the process literally and log each action.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    1 <= target.length <= 100
    1 <= n <= 100
    1 <= target[i] <= n
    target is strictly increasing   -> values go up, never repeat. This lets us
                                       sweep the stream once in lockstep.


EDGE CASES (unusual inputs to check)
------------------------------------
- target already matches the start: [1,2,3], n=3 -> all "Push", no pops.
- Stop early: [1,2], n=4 -> ["Push","Push"]; we must NOT read 3 or 4.
- Gaps at the front: [2,3], n=4 -> read 1 (Push,Pop), then 2 (Push), 3 (Push).
- Single target: [1] -> ["Push"].


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Time  O(m), where m = target[-1] (the largest target value, at most n).
  We read each stream number up to the last needed one exactly once.
- Space O(number of operations) for the answer list (not counted as "extra"
  beyond the required output). We keep no other big structures.
"""

from typing import List


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: walk the stream with a target pointer  (CLEAN -- use this)
    # ----------------------------------------------------------------
    #
    # `i` points at the target value we still need (target[i]).
    # `stream` counts up 1, 2, 3, ... (the next number arriving).
    # For each stream number:
    #   - always "Push" (the rules force us to push what we read)
    #   - if it equals the target value we need -> keep it, advance i
    #   - otherwise -> "Pop" it right back off
    # Stop as soon as we've placed every target value (i reaches the end).
    #
    # Time: O(target[-1])   Space: O(#ops)
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ops = []
        i = 0                       # index of the next target value we want
        stream = 1                  # the next number the stream will give us

        while i < len(target):      # keep going until target is fully built
            ops.append("Push")      # rule: every read number is pushed first
            if target[i] == stream:
                i += 1              # we wanted this one -> keep it, go to next target
            else:
                ops.append("Pop")   # not wanted -> drop it back off the top
            stream += 1             # advance the stream to the next number

        return ops

    # ----------------------------------------------------------------
    # SOLUTION 2: loop the stream values directly with a set lookup
    # ----------------------------------------------------------------
    #
    # Same simulation, expressed by sweeping stream = 1..target[-1] and asking
    # "is this stream number in target?" (membership check via a set).
    # We only need to go up to the LAST target value; nothing after it matters.
    #
    # `set(target)` lets us check "is x wanted?" instantly.
    # `target[-1]` is the LAST element of the list (Python negative indexing:
    #  -1 means "from the end, first one back" = the last item).
    #
    # Time: O(target[-1])   Space: O(n) for the set
    def buildArray_set(self, target: List[int], n: int) -> List[str]:
        wanted = set(target)        # values we must keep
        last = target[-1]           # we can stop once we pass the biggest target
        ops = []
        for stream in range(1, last + 1):   # stream numbers 1..last
            ops.append("Push")              # always push what we read
            if stream not in wanted:
                ops.append("Pop")           # not in target -> remove it
        return ops

    # ----------------------------------------------------------------
    # SOLUTION 3: derive ops from the GAPS between consecutive targets
    # ----------------------------------------------------------------
    #
    # Insight: between one target value and the next, the missing stream numbers
    # each cost a "Push","Pop" (read and discard), and each target value itself
    # costs one "Push". We can compute that directly.
    #
    # `prev` tracks the last value we placed. For each target value t:
    #   - the numbers prev+1 .. t-1 are unwanted -> each adds "Push","Pop"
    #   - then t itself adds "Push"
    #
    # Same result, just builds the list a chunk at a time. Good for seeing the
    # structure ("gaps cost push+pop, hits cost push"). Solution 1 is simpler to
    # write in an interview, though.
    #
    # Time: O(target[-1])   Space: O(#ops)
    def buildArray_gaps(self, target: List[int], n: int) -> List[str]:
        ops = []
        prev = 0                    # we have placed nothing yet (values start at 1)
        for t in target:
            gap = t - prev - 1      # how many unwanted numbers sit before t
            ops.extend(["Push", "Pop"] * gap)   # discard each unwanted number
            ops.append("Push")                  # keep t itself
            prev = t
        return ops


# =====================================================================
# LOCAL TESTING
# =====================================================================
# Any valid sequence is accepted by LeetCode, but the rules here force a
# UNIQUE minimal sequence, so we can compare against exact expected outputs.
if __name__ == "__main__":
    s = Solution()

    # Each entry: (target, n, expected operations)
    tests = [
        ([1, 3],    3, ["Push", "Push", "Pop", "Push"]),
        ([1, 2, 3], 3, ["Push", "Push", "Push"]),
        ([1, 2],    4, ["Push", "Push"]),                 # edge: stop early
        ([2, 3, 4], 4, ["Push", "Pop", "Push", "Push", "Push"]),  # gap at front
        ([1],       1, ["Push"]),                          # edge: single target
    ]

    methods = [
        s.buildArray,
        s.buildArray_set,
        s.buildArray_gaps,
    ]

    for target, n, expected in tests:
        for m in methods:
            assert m(list(target), n) == expected, f"{m.__name__} failed on {target}"

    print("all tests pass")
