# 02 — Build a Neural Network From Scratch (the most important exercise)

If you only deeply understand ONE thing in this whole folder, make it this file.
Once you've built a neural net by hand, every later topic (transformers, LLMs,
fine-tuning) becomes "the same idea, bigger." People who skip this stay confused
forever; people who do it stop being afraid of the math.

We'll build a network that learns the **XOR** problem using only `numpy`.

---

## What is a neural network, in one picture?

A neural network is layers of "neurons." Each neuron does a stunningly simple
thing:

```
neuron output = activation( dot(inputs, weights) + bias )
```

Break that down:
- `inputs` = the numbers coming in (a vector).
- `weights` = the numbers the neuron *learned* (a vector). How much it cares
  about each input.
- `dot(inputs, weights)` = weighted sum (remember the dot product file!).
- `+ bias` = a constant nudge, lets the neuron shift its threshold.
- `activation(...)` = a "squishing" function that adds non-linearity (explained below).

Stack many neurons into a **layer**. Stack many layers, and the output of one
layer is the input to the next. That's a neural network. "Deep" learning just
means "many layers."

```
input ->  [layer 1] -> [layer 2] -> ... -> [output layer] -> prediction
            (neurons)    (neurons)            (neurons)
```

---

## Why do we need "activation functions"?

If every neuron only did `dot + bias` (a straight line), then stacking layers
would still just be one big straight line — the network couldn't learn curvy,
complicated patterns. The **activation function** bends the line, letting the
network model complex shapes.

Two you'll see constantly:

- **Sigmoid**: squishes any number into the range (0, 1). Smooth S-curve. Good
  for "probability-like" outputs.
- **ReLU** (Rectified Linear Unit): `max(0, x)`. If input is negative, output 0;
  otherwise pass it through. Dead simple, and it's what most modern nets use
  because it trains fast.

```
sigmoid(x) = 1 / (1 + e^(-x))      # outputs between 0 and 1
relu(x)    = max(0, x)             # negatives become 0
```

---

## The XOR problem (why it's the classic first test)

XOR ("exclusive or") outputs 1 only when the two inputs differ:

```
input    -> output
(0, 0)   ->   0
(0, 1)   ->   1
(1, 0)   ->   1
(1, 1)   ->   0
```

This is famous because you **cannot** solve it with a single straight line — you
need a hidden layer + activation (non-linearity). If your network learns XOR,
it has genuinely learned something a simple formula can't do. 

---

## The full code (type it out, then run it)

```python
import numpy as np

# ---------- 1. the data ----------
# 4 examples, each with 2 features (the XOR truth table)
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]], dtype=float)
y = np.array([[0],
              [1],
              [1],
              [0]], dtype=float)   # the correct answers

# ---------- 2. activation functions ----------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(s):
    # derivative of sigmoid, given its OUTPUT s
    return s * (1 - s)

# ---------- 3. set up the network ----------
np.random.seed(42)                 # reproducible randomness
input_size  = 2                    # 2 inputs (the two XOR bits)
hidden_size = 4                    # 4 neurons in the hidden layer
output_size = 1                    # 1 output (the predicted bit)

# weights start RANDOM — the network knows nothing yet
W1 = np.random.randn(input_size, hidden_size)   # input  -> hidden
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)  # hidden -> output
b2 = np.zeros((1, output_size))

lr = 0.5                           # learning rate (step size)

# ---------- 4. the training loop ----------
for epoch in range(10000):
    # ----- FORWARD PASS: make a prediction -----
    z1 = X @ W1 + b1               # @ is matrix multiply (batch dot products)
    a1 = sigmoid(z1)               # hidden layer activations
    z2 = a1 @ W2 + b2
    a2 = sigmoid(z2)               # final prediction (between 0 and 1)

    # ----- MEASURE ERROR -----
    error = a2 - y                 # how far off we are
    loss = np.mean(error ** 2)     # mean squared error (one number)

    # ----- BACKWARD PASS: who caused the error? (backpropagation) -----
    # this is the "feel the slope" step from the math file, done with chain rule
    d_a2 = error * sigmoid_deriv(a2)
    d_W2 = a1.T @ d_a2
    d_b2 = np.sum(d_a2, axis=0, keepdims=True)

    d_a1 = (d_a2 @ W2.T) * sigmoid_deriv(a1)
    d_W1 = X.T @ d_a1
    d_b1 = np.sum(d_a1, axis=0, keepdims=True)

    # ----- UPDATE: step every weight downhill -----
    W2 -= lr * d_W2
    b2 -= lr * d_b2
    W1 -= lr * d_W1
    b1 -= lr * d_b1

    if epoch % 1000 == 0:
        print(f"epoch {epoch:5d}  loss {loss:.4f}")

# ---------- 5. test it ----------
print("\nFinal predictions (should be ~0,1,1,0):")
print(np.round(a2, 3))
```

Run it. You should see the loss fall toward ~0 and the final predictions snap to
roughly `[0, 1, 1, 0]`. **You just trained a neural network.** No PyTorch, no
magic — only the dot products and gradients from the previous file.

---

## What just happened (in plain words)

1. **Forward pass:** data flows in, gets multiplied by weights, squished by
   activations, out comes a prediction. At first it's garbage (random weights).
2. **Loss:** we measure how wrong the prediction is — one number.
3. **Backward pass (backpropagation):** we work *backwards* through the network
   asking "how much did each weight contribute to the error?" That's the
   gradient. This is just the chain rule from calculus, applied layer by layer.
4. **Update:** nudge every weight a small step in the direction that reduces
   error (gradient descent).
5. **Repeat 10,000 times.** The weights slowly organize themselves into a
   configuration that solves XOR.

That five-step loop — **forward, loss, backward, update, repeat** — is the
engine inside *every* deep learning model, including Claude and GPT. The
difference is only scale: billions of weights instead of a dozen, and the data
is text instead of a truth table.

---

## The same thing in PyTorch (so you see what libraries give you)

You won't hand-write backprop in real life. PyTorch computes gradients for you
(`autograd`). Same network:

```python
import torch
import torch.nn as nn

X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float32)
y = torch.tensor([[0],[1],[1],[0]], dtype=torch.float32)

model = nn.Sequential(
    nn.Linear(2, 4), nn.Sigmoid(),
    nn.Linear(4, 1), nn.Sigmoid(),
)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.5)

for epoch in range(10000):
    pred = model(X)               # forward
    loss = loss_fn(pred, y)       # measure
    opt.zero_grad()
    loss.backward()               # backward (autograd does the calculus!)
    opt.step()                    # update

print(model(X).round())
```

Notice: `loss.backward()` replaced ALL your hand-written gradient math. That's
what a framework buys you. But because you did it by hand first, you *know* what
that one line is really doing. That knowledge is your edge.

---

## Next step up: do Karpathy's course

The single best free resource to cement this: **Andrej Karpathy — "Neural
Networks: Zero to Hero"** (YouTube + GitHub). He builds:
- `micrograd` — autograd from scratch (same idea you just did, generalized),
- `makemore` — a character-level language model,
- and finally a tiny GPT.

Do it after this file. It bridges you straight into folder 02 (LLMs).

---

## Connection to AI safety

Notice the weights ended up as a pile of numbers that *works* but isn't
human-readable. Look at your final `W1`, `W2` — can you tell what each number
"means"? No. Even in this 17-weight toy, the learned solution is opaque. Now
imagine **billions** of weights. That opacity is exactly why
**interpretability** (folder 06) is hard and important: we can build these
systems far more easily than we can understand them.

---

## Check yourself

1. Name the 5 steps of the training loop, in order.
2. Why do we need a non-linear activation function?
3. In the PyTorch version, which single line replaced all your gradient math?

Next folder: [`../02-llm-internals/00-tokenization.md`](../02-llm-internals/00-tokenization.md)
