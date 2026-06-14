r"""
=====================================================================
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
=====================================================================

THE PROBLEM (in plain words)
----------------------------
You get a math expression written in "Reverse Polish Notation" (RPN), given as
a list of string tokens. Compute its value and return it as an integer.

In normal math we write the operator BETWEEN the numbers:   2 + 1
In RPN we write the operator AFTER the two numbers:          2 1 +
RPN needs no parentheses -- the order alone tells you what to do.

    tokens = ["2","1","+","3","*"]   means  ((2 + 1) * 3) = 9
    tokens = ["4","13","5","/","+"]  means  (4 + (13 / 5)) = 4 + 2 = 6


THE KEY IDEA: a STACK does this perfectly
-----------------------------------------
Read tokens left to right:
  - if the token is a NUMBER -> push it on the stack (set it aside for later).
  - if the token is an OPERATOR (+ - * /) -> the two most-recent numbers are
    its operands. Pop the top two, apply the operator, push the result back.
At the end, exactly one number remains on the stack -> that's the answer.

Walk-through for ["2","1","+","3","*"]:
    "2" -> push        stack: [2]
    "1" -> push        stack: [2, 1]
    "+" -> pop 1, pop 2 -> 2+1=3 -> push   stack: [3]
    "3" -> push        stack: [3, 3]
    "*" -> pop 3, pop 3 -> 3*3=9 -> push   stack: [9]
    answer = 9

WHY a stack? An operator always acts on the TWO most-recently-seen numbers.
"Most recent" = top of the stack. That LIFO (last-in-first-out) behavior is
exactly what RPN evaluation needs. This is THE textbook use of a stack.


THE ORDER TRAP (very important)
-------------------------------
When we pop two values for a "-" or "/", ORDER MATTERS.
The FIRST pop is the RIGHT operand, the SECOND pop is the LEFT operand,
because the right one was pushed most recently (it sits on top).

    tokens [.., a, b, "-"]   ->   result is  a - b   (NOT b - a)
    so:  b = stack.pop()  (top, the right side)
         a = stack.pop()  (next, the left side)
         result = a - b


THE DIVISION TRAP (Python-specific, easy to get wrong)
------------------------------------------------------
The problem says division TRUNCATES TOWARD ZERO:
    7 / 2  = 3        (drop the .5)
   -7 / 2  = -3       (truncate toward zero, NOT down to -4)
    6 / -132 = 0      (see Example 3)

Python's `//` operator does FLOOR division (rounds DOWN toward negative
infinity), so  -7 // 2 == -4  and  6 // -132 == -1  -- WRONG for this problem.
Fix: use  int(a / b).  Python's int() chops the decimal part, which truncates
TOWARD ZERO -- exactly what we need.
    int(-7 / 2) == int(-3.5) == -3        # correct
    int(6 / -132) == int(-0.045...) == 0  # correct


WORDS / IDEAS YOU NEED
----------------------
- TOKEN: one piece of the input, here a string like "2", "+", or "-11".
- OPERAND: a number an operator works on. "+" has two operands.
- We must turn number STRINGS into actual ints with int("12") -> 12.
  int() also understands a leading minus: int("-11") -> -11.


CONSTRAINTS (rules the input always follows)
--------------------------------------------
    1 <= tokens.length <= 10000
    each token is "+", "-", "*", "/", or an integer string in [-200, 200]
    no division by zero; the expression is always valid; results fit in 32 bits.


EDGE CASES (unusual inputs to check)
------------------------------------
- Single number: ["42"] -> 42  (no operators at all)
- Negative numbers as tokens: "-11" must parse as -11, not as a minus operator.
- Truncation toward zero with negatives: ["6","-132","/"] -> 0 (not -1).
- Subtraction order: ["3","4","-"] -> 3-4 = -1 (not 1).


SPEED & MEMORY (time / space complexity)
----------------------------------------
- Time  O(n): we look at each token once; push/pop are instant.
- Space O(n): in the worst case the stack holds about half the tokens (all the
  numbers) before operators start collapsing them.
"""

from typing import List


class Solution:

    # ----------------------------------------------------------------
    # SOLUTION 1: explicit stack with clear if/elif  (LEARN THIS ONE)
    # ----------------------------------------------------------------
    #
    # A Python list doubles as a stack:
    #   stack.append(x)  = push x on top
    #   stack.pop()      = remove & return the top
    #
    # For each token: number -> push; operator -> pop two, combine, push back.
    #
    # Time: O(n)   Space: O(n)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}     # a set for a fast "is it an operator?" check

        for token in tokens:
            if token in operators:
                # pop ORDER matters: top is the right operand, next is the left
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:  # token == "/"
                    # int(a / b) truncates toward zero (NOT floor) -> required here
                    stack.append(int(left / right))
            else:
                # it's a number string (maybe negative like "-11") -> make it an int
                stack.append(int(token))

        # exactly one value remains: the final result
        return stack[0]

    # ----------------------------------------------------------------
    # SOLUTION 2: same stack, but operators stored in a lookup table
    # ----------------------------------------------------------------
    #
    # Instead of an if/elif chain, map each operator symbol to a tiny function
    # that does the math. "lambda a, b: a + b" is a one-line function: given a
    # and b, return a + b. Cleaner when you have many operators.
    #
    # `import operator` could also supply these, but explicit lambdas keep the
    # truncating division obvious.
    #
    # Time: O(n)   Space: O(n)
    def evalRPN_map(self, tokens: List[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),   # truncate toward zero
        }

        stack = []
        for token in tokens:
            if token in ops:
                right = stack.pop()         # top  = right operand
                left = stack.pop()          # next = left operand
                stack.append(ops[token](left, right))
            else:
                stack.append(int(token))
        return stack[0]

    # ----------------------------------------------------------------
    # SOLUTION 3: robust number check (handles any integer, not just symbols)
    # ----------------------------------------------------------------
    #
    # Same algorithm, but instead of asking "is this an operator?", we ask
    # "is this NOT a number?". A token is a number if it's digits, optionally
    # with a leading "-". We test that with a small helper.
    #
    # Why bother? It makes the "is this a number?" decision explicit and avoids
    # accidentally treating a stray symbol as a number. Functionally identical
    # for valid input; good habit for parsing problems.
    #
    # Time: O(n)   Space: O(n)
    def evalRPN_check(self, tokens: List[str]) -> int:
        def is_number(tok: str) -> bool:
            # "-11" -> strip a leading minus, then the rest must be all digits
            return tok.lstrip("-").isdigit()

        stack = []
        for token in tokens:
            if is_number(token):
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                else:
                    stack.append(int(left / right))
        return stack[0]


# =====================================================================
# LOCAL TESTING
# =====================================================================
if __name__ == "__main__":
    s = Solution()

    # Each entry: (tokens, expected integer value)
    tests = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["42"], 42),                       # edge: single number
        (["3", "4", "-"], -1),              # edge: subtraction order (3-4)
        (["6", "-132", "/"], 0),            # edge: truncate toward zero, not -1
        (["-7", "2", "/"], -3),             # edge: negative truncation (not -4)
    ]

    methods = [
        s.evalRPN,
        s.evalRPN_map,
        s.evalRPN_check,
    ]

    for tokens, expected in tests:
        for m in methods:
            assert m(list(tokens)) == expected, f"{m.__name__} failed on {tokens}"

    print("all tests pass")
