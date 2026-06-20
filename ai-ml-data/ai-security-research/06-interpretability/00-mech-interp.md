# 00 — Mechanistic Interpretability: Reading the Model's Mind

This is one of Anthropic's biggest research bets, and possibly the most exciting
area for a newcomer. **Mechanistic interpretability (mech interp)** tries to
**reverse-engineer** a neural network — to understand the actual algorithms and
concepts encoded in its weights, the way you might decompile a program into
readable source code.

If folder 04 showed *we can't inspect what the model learned*, interpretability is
the field trying to fix exactly that.

---

## Why bother? (the motivation)

We can *build* models far more easily than we can *understand* them. We train
billions of weights and get behavior, but the weights are an inscrutable pile of
numbers (remember your tiny XOR net — even 17 weights were unreadable). This
opacity causes nearly every safety problem:

- Is the model **deceptive** (Sleeper Agents, folder 04)? Behavior tests might miss
  it — but maybe we could *see* a deception mechanism inside.
- Did it learn the **right goal** or a lookalike (folder 03)? Look inside and check.
- Is it about to do something harmful? Maybe we can **monitor** internal signals.
- Why did it fail / hallucinate? Trace the actual computation.

> The dream: turn "we hope it's safe because it passed our tests" into "we
> *understand* why it's safe (or not) because we can read its internal
> computation." That's why interpretability is sometimes called a foundation for
> trustworthy AI.

---

## The core idea: features and circuits

Two foundational concepts (from Anthropic's "Circuits" line of work):

- **Features** = the *concepts* a model represents internally. A feature might
  correspond to "the Golden Gate Bridge," "this code is in Python," "the text is in
  French," "the user seems angry," or even abstract things like "this is deceptive."
  Features are the model's vocabulary of meaning.

- **Circuits** = the *computations* connecting features — how the model combines
  earlier features to compute later ones. Like a wiring diagram or a little
  algorithm implemented in the weights. ("If feature A and feature B are active,
  boost feature C.")

The research program: identify the features, map the circuits, and thereby
*explain* how the model produces its behavior — concept by concept, step by step.

---

## A famous concrete result: induction heads

The clearest "we found a real algorithm inside" result. Some attention heads
(folder 02) implement **induction**: completing patterns by copying.

If the context contains `... [A][B] ... [A]`, an **induction head** notices the
earlier `[A][B]` and predicts `[B]` again after the new `[A]`. In plain terms:
*"this pattern appeared before; if it's starting again, copy what followed last
time."*

```
context: "...the cat sat... the cat ___"
induction head: saw "cat" -> "sat" before; sees "cat" again -> predict "sat"
```

Why it's a big deal:
- It's a **human-understandable algorithm** found *inside* a trained Transformer —
  proof that mech interp can actually succeed.
- Induction heads are strongly linked to **in-context learning** (the model's
  ability to learn from examples in the prompt) — which ties back to many-shot
  jailbreaking (folder 04-02) and to how LLMs generalize. Understanding the
  mechanism connects capability and safety.

---

## Superposition: why interpretability is hard

Here's the twist that makes it difficult. You'd hope each neuron = one clean
concept. Reality: models pack **more features than they have neurons** by storing
them in overlapping combinations — called **superposition** (Anthropic's "Toy
Models of Superposition"). So a single neuron lights up for *several unrelated*
concepts ("polysemantic" neurons), and concepts are smeared across many neurons.

Analogy: imagine trying to store 1000 distinct ideas using only 100 light switches
by using *patterns* of switches rather than one switch per idea. Efficient for the
model, a nightmare to decode.

This is why you can't just read neurons one by one. You need a tool to *untangle*
superposition — which leads to the current frontier.

---

## Sparse Autoencoders (SAEs): the current breakthrough tool

To pull apart superposition, researchers use **Sparse Autoencoders (SAEs)**. The
idea (conceptually):
- Train a small helper network that takes the model's internal activations and
  re-expresses them as a **much larger but sparse** set of features — sparse meaning
  only a few are active at once.
- This tends to recover **monosemantic** features — each one cleanly corresponds to
  a single human-interpretable concept — disentangling the superposition.

Milestones to know:
- *"Towards Monosemanticity"* (Anthropic, 2023): SAEs extract clean features from a
  small model.
- *"Scaling Monosemanticity"* (Anthropic, 2024): scaled SAEs to a *production* model
  (Claude 3 Sonnet), extracting millions of features — including abstract and
  safety-relevant ones (e.g. features for deception, sycophancy, dangerous content,
  and the famous "Golden Gate Bridge" feature they could *turn up* to make Claude
  obsessively talk about the bridge). Being able to **find and steer** a concept's
  feature is a direct safety lever.

> "Golden Gate Claude" wasn't a gimmick — it demonstrated **causal control**: find
> the feature, amplify it, watch behavior change predictably. If you can do that
> with a "deception" or "harmful intent" feature, you have a monitoring/steering
> tool for safety.

---

## What interpretability could give us (the safety payoff)

- **Lie detection / deception monitoring:** spot when an internal "deception"
  feature activates.
- **Backdoor detection:** find the hidden trigger circuit (folder 04) by inspection
  rather than hoping behavior tests catch it.
- **Auditing values:** verify the model represents the goals we intended.
- **Steering:** turn features up/down to adjust behavior precisely, beyond blunt
  fine-tuning.
- **Early warning:** detect dangerous capabilities forming during training.

Caveat (be honest): interpretability is **early**. We can't yet fully reverse-
engineer a frontier model, SAEs miss things, and "we found a feature" isn't the
same as "we understand the whole model." That gap is the open frontier — and the
opportunity.

---

## Hands-on: this is very approachable for beginners

Great news: you can do real interpretability on *small* models on a laptop.

- **TransformerLens** (library by Neel Nanda) is built for exactly this: load a
  small GPT-2-style model and inspect/intervene on its internals (attention
  patterns, activations, ablations).
- **Neel Nanda's "200 Concrete Open Problems in Mechanistic Interpretability"** and
  his tutorials are the standard on-ramp. Many problems are beginner-friendly and
  publishable.

```bash
pip install transformer-lens torch
```

Starter project (`10-projects/`):
1. Load a small model in TransformerLens.
2. Find evidence of an **induction head** (feed it a repeated random sequence and
   see which heads predict the repeat).
3. **Ablate** (zero out) that head and show the prediction breaks — proving the
   head *causes* the behavior.
4. Write it up. This is a legitimate, classic interpretability exercise and a
   strong portfolio piece.

---

## Why this is THE area to consider for an Anthropic-style fellowship

- It's central to Anthropic's strategy (they bet heavily on it).
- It's young — you can reach the frontier in months, not years.
- It rewards careful experiment design and clear thinking over heavy prerequisites.
- Real results are achievable on small models / modest compute.
- There's a welcoming community and curated open problems.

If any single folder makes you feel "I want to do *that*," and it's this one,
lean in.

---

## Check yourself

1. What are "features" and "circuits"?
2. Explain an induction head in one sentence.
3. What is superposition, and why does it make interpretability hard?
4. What problem do SAEs solve, and what did "Scaling Monosemanticity" show?
5. Why is interpretability considered important for *detecting deception*?

Next folder: [`../07-evals-and-oversight/00-evals-and-oversight.md`](../07-evals-and-oversight/00-evals-and-oversight.md)
