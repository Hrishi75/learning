# 01 — The Minimum Math You Actually Need (taught gently)

Many beginners freeze here. Don't. You do **not** need to master university math
before touching ML. You need a working *intuition* for four things, and you can
learn the rest exactly when a problem forces you to.

The four things:
1. Vectors and matrices (how we store data and weights)
2. The dot product (the single most-used operation in all of deep learning)
3. Derivatives / gradients (how a model knows which way to improve)
4. Probability basics (how a model expresses uncertainty)

Let's take them one at a time, with pictures and tiny numbers.

---

## 1. Vectors and matrices = just lists and grids of numbers

A **vector** is an ordered list of numbers. That's all.

```
v = [2, 5, 1]      # a vector with 3 numbers
```

Why we care: everything in ML becomes numbers. A word becomes a vector. An image
becomes a vector. A user becomes a vector. We call the length the
**dimension** — `[2, 5, 1]` is 3-dimensional.

A **matrix** is a grid (rows × columns) of numbers — basically a list of vectors:

```
M = [[1, 2, 3],
     [4, 5, 6]]    # a 2x3 matrix: 2 rows, 3 columns
```

Why we care: the "knowledge" a neural network learns is stored as big matrices of
numbers called **weights**. Training = slowly adjusting those numbers.

**Analogy:** a spreadsheet is a matrix. A single row is a vector. You already
understand spreadsheets — you already understand the storage part of ML.

---

## 2. The dot product = "how much do two vectors agree?"

This is THE operation. Memorize how it works; you'll see it everywhere.

Take two vectors of the same length. Multiply them element-by-element, then add
it all up:

```
a = [1, 2, 3]
b = [4, 0, 5]

dot(a, b) = (1*4) + (2*0) + (3*5)
          =   4   +   0   +  15
          = 19
```

In Python/numpy:

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 0, 5])
print(np.dot(a, b))   # -> 19
```

**What does the number mean?** It measures *alignment / similarity*.
- Big positive number -> the vectors "point the same way" -> they're similar.
- Zero -> unrelated (perpendicular).
- Negative -> they point opposite ways.

**Why you care:** when an LLM decides "how relevant is word A to word B?", it
literally computes a dot product between their vectors. Attention (folder 02) is
mostly dot products. Recommendation ("users like you also liked...") is dot
products. Get comfortable here.

A **matrix multiplication** is just *a whole bunch of dot products done at once.*
Don't fear the term "matmul" — it's batch dot products.

---

## 3. Derivatives and gradients = "which way is downhill?"

This is how a model *learns*. Here's the whole idea with an analogy.

Imagine you're standing on a foggy hill, blindfolded, and you want to reach the
lowest point (the valley). You can't see, but you *can* feel the slope under your
feet. Strategy:

1. Feel which direction goes **downhill**.
2. Take a small step that way.
3. Repeat until the ground is flat (you're at the bottom).

That's literally how models train. Replace the words:

- **The hill** = the model's *error* (how wrong it is). High = very wrong.
- **The valley** = low error = a good model.
- **The slope you feel** = the **gradient** (a derivative).
- **Step downhill** = **gradient descent**, the core training algorithm.

A **derivative** answers: *"if I nudge this number up a tiny bit, does the error
go up or down, and by how much?"* The **gradient** is just all those derivatives
bundled together (one per weight in the model).

Tiny concrete example. Say error as a function of one weight `w` is:

```
error(w) = (w - 3)^2
```

This is a U-shaped curve with its lowest point at `w = 3`. The derivative is
`2*(w - 3)`:

- At `w = 0`: derivative = `2*(0-3) = -6`. Negative slope -> go **up** in w to
  reduce error. So we increase w. Good — moving toward 3.
- At `w = 5`: derivative = `2*(5-3) = +4`. Positive slope -> decrease w. Also
  toward 3. 

The training loop, in words:

```
repeat many times:
    1. run the model, measure the error
    2. compute the gradient (slope) for every weight
    3. nudge each weight a small step "downhill"
```

The "small step" size is called the **learning rate**. Too big = you overshoot
the valley and bounce around. Too small = you take forever. Tuning it is an art.

You will rarely compute derivatives by hand — libraries like PyTorch do it
automatically (called **autograd** / **backpropagation**). But you must *picture*
the foggy hill. That picture is 90% of the intuition.

---

## 4. Probability basics = how a model says "I'm 70% sure"

Models rarely output a hard yes/no. They output **probabilities** — numbers
between 0 and 1 that sum to 1 across the choices.

Example: an LLM predicting the next word doesn't say "the answer is *mat*." It
says:

```
mat   : 0.61
rug   : 0.25
floor : 0.10
banana: 0.04
        -----
total : 1.00   (always sums to 1)
```

Two terms you'll meet constantly:

- **Softmax**: a function that turns any list of raw scores (called *logits*)
  into clean probabilities that sum to 1. The model produces raw scores; softmax
  makes them a probability distribution.
- **Temperature**: a knob on softmax that controls randomness.
  - Low temperature (e.g. 0.2) -> model picks the top choice almost always ->
    *focused, repetitive.*
  - High temperature (e.g. 1.2) -> model spreads probability out -> *creative,
    riskier, more random.*
  - When you change "temperature" in an LLM playground, this is what you're touching.

---

## What you do NOT need (yet)

Skip these until a specific problem demands them. Don't let them block you:
- Eigenvalues, determinants, matrix inverses (rare day-to-day)
- Multivariable calculus proofs
- Measure theory, advanced statistics

Learn-just-in-time. The worst beginner mistake is spending 3 months on math
textbooks and never building anything.

---

## A 30-minute exercise (do it, don't skip)

Open a Python file and play:

```python
import numpy as np

# vectors
a = np.array([1.0, 2.0, 3.0])
b = np.array([0.0, 1.0, 0.0])
print("dot:", np.dot(a, b))            # similarity between a and b

# a tiny "downhill" demo: minimize (w-3)^2 by hand
w = 0.0
lr = 0.1                               # learning rate
for step in range(30):
    grad = 2 * (w - 3)                 # derivative of (w-3)^2
    w = w - lr * grad                  # step downhill
    print(f"step {step:2d}: w = {w:.4f}")
# watch w crawl toward 3.0 — that's gradient descent
```

Run it. Watch `w` approach 3. **That print loop is the heartbeat of all of deep
learning.** Everything else is this same idea at massive scale.

---

## Check yourself

1. What does a dot product *measure*?
2. In the foggy-hill analogy, what are: the hill, the valley, the slope, the step?
3. What does "temperature" change in an LLM's output?

Next: [`02-neural-network-from-scratch.md`](02-neural-network-from-scratch.md) —
build a real (tiny) neural net with the math above.
