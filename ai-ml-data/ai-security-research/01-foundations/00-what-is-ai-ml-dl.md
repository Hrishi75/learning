# 00 — What are AI, ML, and Deep Learning? (start here)

You'll hear "AI", "machine learning", "deep learning", and "LLM" used as if
they're the same thing. They are not. Let's untangle them once, clearly, so you
never get confused again.

---

## The nesting-dolls picture

Think of Russian nesting dolls — each one inside a bigger one:

```
┌───────────────────────────────────────────────────────┐
│ ARTIFICIAL INTELLIGENCE (AI)                            │
│  "Machines doing things that seem intelligent"          │
│  ┌─────────────────────────────────────────────────┐   │
│  │ MACHINE LEARNING (ML)                            │   │
│  │  "Machines that learn from data, not from rules" │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │ DEEP LEARNING (DL)                         │  │   │
│  │  │  "ML using many-layered neural networks"   │  │   │
│  │  │  ┌──────────────────────────────────────┐  │  │   │
│  │  │  │ LLMs (Large Language Models)         │  │  │   │
│  │  │  │  "DL trained on huge amounts of text"│  │  │   │
│  │  │  │   e.g. Claude, GPT, Gemini, Llama    │  │  │   │
│  │  │  └──────────────────────────────────────┘  │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
└───────────────────────────────────────────────────────┘
```

- **AI** is the broadest dream: machines that act intelligently. A chess program
  with hand-written rules is AI, even though it never "learns."
- **ML** is one *way* to do AI: instead of a human writing the rules, the machine
  figures out the rules **from examples (data)**.
- **DL** is one *kind* of ML: it uses **neural networks** with many layers.
- **LLMs** are a *use* of DL: huge neural networks trained to predict text.

---

## The key idea that makes ML different from normal programming

**Traditional programming:**

```
Rules + Data  ->  Computer  ->  Answers
```

You (the human) write the rules. Example: "IF email contains 'free money' THEN
mark as spam." You wrote that rule by hand.

**Machine learning flips it:**

```
Data + Answers  ->  Computer  ->  Rules (a "model")
```

You give the computer thousands of emails *already labeled* spam / not-spam. The
computer **discovers the rules by itself**. Those discovered rules are called a
**model**. Later you feed a new email into the model and it predicts spam or not.

> This flip is the whole reason ML is powerful: for messy problems (recognizing
> cats, understanding language), nobody knows how to write the rules by hand.
> So we let the machine learn them from examples.

---

## The 3 main flavors of machine learning

### 1. Supervised learning (learn from labeled examples)
You give inputs **and** the correct answers.
- Example: 10,000 photos, each labeled "cat" or "dog." Model learns to tell them apart.
- Example: house features (size, location) + their actual sale prices. Model learns to predict price.
- **Most of what you'll use is supervised-ish.** Even LLMs start here.

### 2. Unsupervised learning (find structure with no labels)
You give only inputs, no answers. The model finds patterns/groups itself.
- Example: group 1 million customers into "types" without telling it the types.

### 3. Reinforcement learning (learn from reward/punishment)
An "agent" takes actions in an environment and gets rewards. It learns the
behavior that maximizes reward over time.
- Example: a program learning to play a game by trying moves and seeing the score.
- **This matters a lot for you** — RLHF (folder 03) uses reinforcement learning
  to make LLMs helpful and harmless.

---

## Where do LLMs fit? (the part you care about most)

An LLM is trained with a deceptively simple task: **predict the next word.**

Give it: `"The cat sat on the ___"`
It learns to predict: `"mat"` (and assigns probabilities to every possible word).

That's it. That single objective — **next-token prediction** — repeated over
*trillions* of words from the internet, books, and code, produces a model that
can write essays, code, translate, and reason. Nobody fully expected this to
work as well as it does. The surprise that "just predict the next word" leads to
apparent reasoning is one of the deepest open questions in the field.

We'll go deep on this in folder 02. For now, hold onto this sentence:

> **An LLM is a giant next-word-prediction machine, and almost everything it can
> do is an emergent side effect of getting really good at that one task.**

---

## A concrete tiny example (no code yet, just intuition)

Imagine a *very* dumb language model that learned from one sentence repeated a lot:

`"I love pizza. I love pasta. I love bread."`

Ask it: `"I love ___"`
It has seen "pizza", "pasta", "bread" follow "I love." So it predicts one of
those, maybe with probabilities like:

```
pizza  : 34%
pasta  : 33%
bread  : 33%
banana :  0%   (never seen it after "I love")
```

A real LLM does exactly this, but with billions of patterns instead of three.

---

## Why this matters for AI safety (the connection)

Because the model learns rules **from data instead of from humans**, we often
**don't know what rules it actually learned.** It might learn:

- a *correct* rule ("spam often has urgent money language"), or
- a *sneaky shortcut* ("emails sent at 3am are spam" — true in the training data
  by accident, but wrong in general).

This gap — *we trained it to do X, but we can't be sure what it really learned* —
is the seed of nearly every AI safety problem:

- **Alignment:** did it learn our real goal, or a lookalike goal?
- **Security:** can an attacker exploit the weird shortcuts it learned?
- **Interpretability:** can we *look inside* and check what it learned?

Keep this in mind. It's the thread that ties this whole folder together.

---

## Check yourself (answer out loud before moving on)

1. In one sentence, how is ML different from traditional programming?
2. What is the one task LLMs are trained on?
3. Why is "we don't know exactly what rule the model learned" a safety problem?

Next: [`01-math-you-need.md`](01-math-you-need.md) — the *minimum* math, taught gently.
