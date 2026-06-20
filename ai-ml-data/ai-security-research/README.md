# AI Security & Safety — Research Notes (from zero)

This folder is your full self-study course to go from **complete beginner** to
someone who can apply for AI safety research fellowships (Anthropic Fellows
Program, MATS, etc.).

You don't need a PhD to start. You need curiosity, consistency, and the
willingness to *implement* things, not just read about them.

---

## How to read this folder

Read the numbered folders **in order**. Each `.md` file is written like a
patient teacher explaining to a smart beginner. Every concept has:

- a plain-English explanation,
- a real-world analogy,
- a concrete example (often with code),
- and "open questions" at the end (research is about questions, not answers).

> Rule for yourself: **never just read.** After each file, type the code out,
> run it, break it, fix it. Understanding comes from your fingers, not your eyes.

---

## The map (what each folder covers)

| #  | Folder | The big question it answers |
|----|--------|------------------------------|
| 01 | foundations | What are AI, ML, and neural networks — really? |
| 02 | llm-internals | How does an LLM like Claude or GPT actually work inside? |
| 03 | alignment | How do we make models do what humans actually want? |
| 04 | ai-security | How do people attack AI systems (and how do we defend)? |
| 05 | red-teaming | How do we *systematically* find a model's failures? |
| 06 | interpretability | Can we look inside a model and understand its "thoughts"? |
| 07 | evals-and-oversight | How do we measure danger and supervise systems smarter than us? |
| 08 | papers | The reading list, with a summary template |
| 09 | fellowship-prep | How to actually apply and build a portfolio |
| 10 | projects | Where YOU put your own reproductions and experiments |

---

## What "AI safety / AI security" even means (30-second version)

- **AI capabilities** = making models *more powerful* (smarter, faster).
- **AI safety / alignment** = making models *do what we intend*, even as they
  get powerful — not lie, not cause harm, not pursue goals we didn't give them.
- **AI security** = protecting AI systems from *attackers* — people who trick,
  poison, or steal models (prompt injection, jailbreaks, data poisoning).

Anthropic's whole mission is the safety side: build powerful AI **and** make
sure it's trustworthy. That's the lens for everything in this folder.

---

## 12-week beginner roadmap

You can go slower. This is a suggested rhythm, ~10-15 hrs/week.

**Weeks 1-2 — Foundations** (folder 01)
- Understand AI vs ML vs deep learning.
- Learn the *minimum* math (don't over-study — learn what you need when you need it).
- Build a neural network from scratch in plain Python/numpy. This is the single
  most important exercise. Do not skip it.

**Weeks 3-4 — LLM internals** (folder 02)
- Tokenization (how text becomes numbers).
- The Transformer and attention (the engine inside every modern LLM).
- How LLMs are trained: pretraining vs fine-tuning, scaling laws.
- Build a tiny GPT (follow Karpathy's nanoGPT — link in folder 02).

**Weeks 5-6 — Alignment** (folder 03)
- What "alignment" means and why it's hard.
- RLHF (Reinforcement Learning from Human Feedback) — how raw models become
  helpful assistants.
- Constitutional AI (Anthropic's method) and DPO.

**Weeks 7-8 — AI security** (folder 04)
- Adversarial examples, prompt injection, jailbreaks, data poisoning.
- Reproduce one simple attack on an open model.

**Weeks 9-10 — Interpretability** (folder 06) + **Red teaming** (folder 05)
- Mechanistic interpretability: induction heads, features, circuits.
- Try the TransformerLens library.

**Weeks 11-12 — Evals, oversight, and YOUR project** (folders 07, 10)
- Dangerous-capability evals, Responsible Scaling Policy.
- Scalable oversight: debate, weak-to-strong generalization.
- Ship ONE small original project + a writeup. This becomes your application.

---

## The tools you'll install (when you reach folder 02)

```bash
pip install numpy torch transformers datasets einops transformer-lens
```

Don't install everything now. Install each when a file tells you to.

---

## Mindset reminders (read these on hard days)

1. **Confusion is the feeling of learning.** If it's easy, you're not growing.
2. **Reproduce before you innovate.** Re-implement known results first.
3. **Negative results are real results.** "It didn't work and here's why" is good science.
4. **Write things down.** The act of explaining (in these files) reveals what you don't understand.
5. **Consistency beats intensity.** 1 hour daily > 10 hours once a week.

Start with [`01-foundations/00-what-is-ai-ml-dl.md`](01-foundations/00-what-is-ai-ml-dl.md).
