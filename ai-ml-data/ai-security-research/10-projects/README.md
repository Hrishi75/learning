# 10 — Projects: Where You Build (the part that gets you in)

Reading teaches; **building proves.** This folder is where YOUR work lives — the
reproductions and experiments that become your fellowship portfolio (folder 09).
Each project = its own subfolder with code + a `WRITEUP.md`.

> Golden rule: **a finished small project beats an unfinished ambitious one.**
> Scope tiny. Finish. Write it up. Repeat.

---

## The project ladder (do roughly in this order)

Each links back to the folder that teaches the concept.

### Level 0 — Warm-ups (build confidence)
- [ ] **Neural net from scratch (numpy XOR)** — folder 01-02. ~50 lines, no
  frameworks. Proves you understand forward/backprop/gradient descent.
- [ ] **nanoGPT** — folder 02. Follow Karpathy; train a tiny char-level GPT on a text
  file (e.g. Shakespeare). Proves you understand Transformers end-to-end.

### Level 1 — Core reproductions (your main portfolio pieces)
- [ ] **DPO fine-tune** — folder 03. Align a small open model on a preference
  dataset; show before/after. Proves you understand alignment in practice.
- [ ] **Find an induction head** — folder 06. Use TransformerLens; locate the head,
  ablate it, show the behavior breaks. Proves interpretability skill.
- [ ] **Adversarial example (FGSM)** — folder 04. Fool an image classifier with
  invisible noise. Proves you understand model fragility + gradients.

### Level 2 — Security / red-team experiments
- [ ] **Prompt-injection demo + defense** — folder 04-01. Tiny email-summarizer
  wrapper; show injection works; add instruction-hierarchy/filter; measure what
  still gets through.
- [ ] **Jailbreak-robustness mini-eval** — folder 04-02 / 05. Measure attack success
  rate across a few transformation categories + over-refusal on benign prompts.
  Report a tradeoff curve.

### Level 3 — Original mini-research (pick ONE, go deeper)
- [ ] An original question of *your own* — small, falsifiable, honestly measured.
  Mine ideas from each file's "open questions" and Neel Nanda's "200 Open Problems"
  (folder 08). Negative results welcome.

You do **not** need all of these. ~3 finished projects (one reproduction, one
security/interp experiment, one original) is a strong application.

---

## Every project needs a WRITEUP.md (use this template)

```markdown
# <Project name>

## Question / goal
<what you set out to do, in one or two sentences>

## Background
<the concept + which paper/folder it comes from; 2-3 sentences>

## Method
<what you actually did — enough that someone could reproduce it>

## Results
<tables / charts / example outputs. Numbers, not vibes.>

## What I learned
<insights, including surprises>

## Limitations & what I'd do next
<be honest and critical — this section signals research maturity>

## How to run
<commands so anyone can reproduce. Pin versions.>
```

The **Limitations** and **What I'd do next** sections matter as much as the
results. They show you think like a researcher, not just a coder.

---

## Standards that make a project "portfolio-grade"

- **Reproducible:** someone can `git clone` and run it. Pin dependencies.
- **Documented:** clear README, commented code where it's non-obvious.
- **Honest:** state what didn't work and what you're unsure about.
- **Small & complete:** finished and clear > sprawling and abandoned.
- **Public:** push to GitHub; consider a short blog post (folder 09) and posting on
  LessWrong/Alignment Forum for feedback.

---

## Suggested folder layout per project

```
10-projects/
  01-nn-from-scratch/
    nn.py
    WRITEUP.md
  02-dpo-finetune/
    train_dpo.py
    results/
    WRITEUP.md
  03-induction-head/
    explore.ipynb
    WRITEUP.md
  ...
```

---

## Now go

You've read the theory. Open folder 01, build the from-scratch net if you haven't,
then climb the ladder. Ship something small this week. Momentum is the whole
secret.

Back to the [course index](../README.md).
