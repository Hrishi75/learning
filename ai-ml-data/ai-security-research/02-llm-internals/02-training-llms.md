# 02 — How LLMs Are Actually Trained (pretraining, fine-tuning, scaling)

You now know the Transformer's shape. This file explains how a useless pile of
random weights becomes Claude. There are **three big stages**, and knowing them
is essential — most alignment and safety work happens in stages 2 and 3.

```
Stage 1: PRETRAINING      -> a raw "knows-everything-but-wild" text predictor
Stage 2: FINE-TUNING(SFT) -> teach it to follow instructions / act like an assistant
Stage 3: ALIGNMENT (RLHF) -> teach it to be helpful, honest, harmless
```

---

## Stage 1 — Pretraining: learn language from the whole internet

**Goal:** learn to predict the next token, over a *massive* amount of text
(trillions of tokens: web pages, books, code, Wikipedia, etc.).

**How:** exactly the training loop from folder 01 (forward, loss, backward,
update), but:
- the model is huge (billions of weights),
- the data is enormous,
- it runs for weeks/months on thousands of GPUs,
- costing millions of dollars.

The model sees text like `"The capital of France is ___"` and is trained to put
high probability on `"Paris"`. Do this over trillions of tokens and it absorbs
grammar, facts, reasoning patterns, coding, translation — all as a side effect of
getting good at next-token prediction.

The result of pretraining is called a **base model** (or "foundation model"). Key
thing to understand: **a base model is NOT a helpful chatbot.** It's a raw text
*completer*. Ask a base model "What is the capital of France?" and it might
reply with more *questions*, because on the internet, questions are often
followed by more questions (like a quiz). It completes text; it doesn't "want" to
help you. Making it helpful is stages 2 and 3.

> Analogy: pretraining is like a person who has read the entire internet but has
> never been told *what to do* with that knowledge or how to behave politely.

---

## Stage 2 — Supervised Fine-Tuning (SFT): teach it to be an assistant

**Goal:** turn the raw completer into something that *follows instructions.*

**How:** show it thousands of high-quality example *conversations* written/curated
by humans:

```
User: What is the capital of France?
Assistant: The capital of France is Paris.

User: Write a haiku about the ocean.
Assistant: Waves whisper softly / ...
```

We run the same next-token training, but now on this curated "this is how a
helpful assistant responds" data. The model learns the *format and behavior* of
being an assistant: answer the question, be polite, follow the instruction.

After SFT you have an "instruct" model that's genuinely useful. But it's still
imperfect — it might be confidently wrong, unhelpful in subtle ways, or willing
to help with harmful requests. That's where stage 3 comes in.

---

## Stage 3 — Alignment via RLHF: make it helpful, honest, harmless

This is the stage most relevant to AI safety, so folder 03 covers it in depth.
Quick preview:

**Goal:** align the model with human preferences — be more helpful, refuse harmful
requests, admit uncertainty.

**How (RLHF = Reinforcement Learning from Human Feedback):**
1. The model generates two answers to a prompt.
2. A human (or another model) picks which answer is better.
3. Collect lots of these comparisons; train a **reward model** to predict human
   preference (a number: "how good is this answer?").
4. Use reinforcement learning to update the LLM so it produces answers the reward
   model scores highly.

This is how "raw smart text predictor" becomes "Claude, the helpful, careful
assistant." Full details in [`../03-alignment/01-rlhf-and-dpo.md`](../03-alignment/01-rlhf-and-dpo.md).

---

## Scaling laws — why bigger really is (predictably) better

A landmark finding (Kaplan et al. 2020; refined by "Chinchilla", Hoffmann et al.
2022): model performance improves **smoothly and predictably** as you increase
three things together:

1. **Parameters** (model size — number of weights),
2. **Data** (number of training tokens),
3. **Compute** (how much processing you throw at it).

Plot performance vs these on a log scale and you get clean straight lines —
**scaling laws**. This is huge because it means you can *predict* how much better
a bigger model will be *before* spending millions to train it. The race to bigger
models is driven by these curves.

The Chinchilla refinement: most early big models were *undertrained* — for a
given compute budget, you should use a **smaller model with more data** than
people assumed. "Compute-optimal" training. Worth reading the Chinchilla paper
later (folder 08).

---

## Emergent abilities — the part that worries safety researchers

As models scale, some abilities appear **suddenly** rather than gradually — the
model is bad at a task at one size, then much bigger models can suddenly do it
(e.g. multi-step arithmetic, certain reasoning). These are **emergent
capabilities**.

Why this matters for safety:
- We **can't fully predict** which new abilities a bigger model will have.
- Some of those abilities could be dangerous (e.g. helping with bio/cyber threats,
  deception, manipulation) and we'd only find out *after* training.
- This is the entire reason for **dangerous capability evaluations** and the
  **Responsible Scaling Policy** (folder 07): test for scary abilities *before*
  release.

> (Note: researchers debate whether "emergence" is real or an artifact of how we
> measure it. That debate itself is a good thing to read about — it's live science.)

---

## A few terms you'll keep hearing (quick glossary)

- **Parameters / weights:** the numbers the model learned. "70B" = 70 billion of them.
- **Tokens:** the text chunks (folder 02-00). Training and context are measured in tokens.
- **Epoch:** one full pass over the training data.
- **Checkpoint:** a saved snapshot of the model's weights at some point in training.
- **Fine-tuning:** continuing training a pretrained model on narrower data to specialize it.
- **Inference:** *using* a trained model to generate output (as opposed to training it).
- **Context window:** how many tokens the model can "see" at once (its short-term memory).

---

## Connection to AI security & safety

- **Pretraining data is an attack surface.** If attackers sneak poisoned text into
  the web data a model trains on, they can plant hidden behaviors (**data
  poisoning / backdoors**, folder 04). You can't manually inspect trillions of tokens.
- **Each stage can introduce or hide problems.** A model might *look* aligned after
  RLHF but harbor behaviors that only trigger in rare conditions ("Sleeper Agents",
  an Anthropic paper — folder 08).
- **Alignment is a *training-time* problem.** Stages 2-3 are literally "how do we
  shape behavior?" — which is the central question of AI safety.

---

## Check yourself

1. What's the difference between a base model and an instruct/chat model?
2. Why won't a raw base model behave like a helpful assistant?
3. What are the three things scaling laws relate, and why are they useful?
4. Why do emergent capabilities make pre-release evaluations important?

Next folder: [`../03-alignment/00-what-is-alignment.md`](../03-alignment/00-what-is-alignment.md)
