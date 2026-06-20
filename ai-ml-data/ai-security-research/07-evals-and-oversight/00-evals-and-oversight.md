# 00 — Evaluations, Dangerous Capabilities & Scalable Oversight

Two big topics that complete your safety picture:
1. **Evals** — how we *measure* what a model can do and how safe it is (including
   testing for dangerous capabilities *before* release).
2. **Scalable oversight** — how we *supervise* models that may become smarter than
   the humans judging them.

Both are central to how Anthropic decides whether a model is safe to deploy.

---

## Part 1 — Evaluations ("evals")

### What an eval is
An **eval** is a structured test that measures a model's behavior on some
dimension: a capability (math, coding, reasoning), a safety property (refusal
robustness, bias, honesty), or a dangerous capability (can it meaningfully help
with bio/cyber/weapons, deception, or autonomous replication?).

Think "exams for AIs," but designed with the rigor of science: defined tasks, a
scoring rubric, a dataset, and reproducible methodology.

### Why evals are harder than they sound
- **Measuring capabilities is tricky.** A model might fail a task because it *can't*
  do it, or because of bad prompting. "Absence of evidence isn't evidence of
  absence" — failing your test doesn't prove the capability is absent; a better
  prompt might unlock it. This makes *safety* evals (proving something is NOT there)
  genuinely hard.
- **Contamination.** If the test questions leaked into training data, high scores
  are fake (the model memorized the answers). Detecting/avoiding contamination is a
  real subfield.
- **Goodhart's law.** "When a measure becomes a target, it stops being a good
  measure." Once an eval becomes a benchmark everyone optimizes, scores inflate
  without real improvement (echoes reward hacking, folder 03).
- **Capability elicitation.** To safely claim "the model can't do X," you must try
  *hard* to make it do X (good prompting, fine-tuning, tools). Weak elicitation =
  false sense of safety.

### Dangerous capability evaluations (the high-stakes kind)
Before releasing a frontier model, labs test for capabilities that could cause
serious harm, e.g.:
- meaningful uplift to **bioweapon / chemical / cyber** attack planning,
- **autonomous** abilities (self-replication, acquiring resources, evading
  shutdown),
- advanced **deception / manipulation**, situational awareness.

These evals decide whether — and with what safeguards — a model ships. They're done
carefully, often with domain experts, and feed directly into the policy below.

### Responsible Scaling Policy (RSP) & ASL levels
Anthropic's **Responsible Scaling Policy** ties deployment to measured risk. The
core mechanism: **AI Safety Levels (ASL)**, modeled loosely on biosafety levels
(BSL-1..4). Roughly:
- Higher ASL = more dangerous demonstrated capabilities = stricter required
  safeguards (security, deployment limits, evals) *before* training/releasing.
- If a model crosses a capability threshold without adequate safeguards ready, the
  policy says **pause** until safeguards catch up.

The big idea: **scale capability and safety together**, and let *measurements*
(evals) gate decisions rather than vibes. Read Anthropic's current RSP (it's
updated over time) — it's a concrete example of governance grounded in evals.
Similar ideas: OpenAI's Preparedness Framework, Google DeepMind's Frontier Safety
Framework. Know that these exist.

---

## Part 2 — Scalable Oversight

### The problem
RLHF (folder 03) relies on **humans judging** model outputs. But what happens when
the model is *better than the human* at the task? How do you give good feedback on:
- a 10,000-line program you can't fully review,
- a scientific claim in a field you don't know,
- a subtly flawed argument more sophisticated than you could produce?

If we can't reliably supervise systems smarter than us, RLHF-style alignment breaks
down right when it matters most. **Scalable oversight** = research on supervising
models *at or beyond human capability.* Several approaches:

### Approach 1 — Decompose the task (recursive)
Break a task too hard to judge into smaller pieces a human *can* judge, possibly
using AI assistants to help evaluate each piece. ("Task decomposition" / iterated
amplification flavors.) Intuition: you can't grade the whole essay, but you can
check each cited fact if it's broken out.

### Approach 2 — AI Debate
Have **two AI systems argue opposite sides** of a question in front of a human (or
AI) judge. The bet: it's easier to *judge a debate* than to find the truth yourself,
because each side is incentivized to expose the other's flaws — lies get rebutted.
(Irving et al., "AI Safety via Debate.") Open question: does this actually converge
on truth, or on *persuasiveness*? Active research.

### Approach 3 — AI-assisted evaluation (CAI is an example)
Use AI to *help humans* supervise — e.g. Constitutional AI (folder 03) uses AI
feedback guided by human-written principles. The human supervises the *process and
principles*; the AI scales the labor.

### Approach 4 — Weak-to-strong generalization
A striking research direction (OpenAI, 2023): can a **weak supervisor** (or weak
labels) successfully train a **stronger** student model — and have the strong model
generalize *beyond* the weak teacher's mistakes? This is an analogy for *humans
(weak) supervising superhuman models (strong).* Early experiments show the strong
student can partly exceed its weak teacher, but not perfectly. A promising, very
researchable thread.

---

## How it all ties together (zoom out)

```
Capabilities grow  ->  Evals measure capability & danger  ->  RSP/ASL gates deployment
                                          |
Alignment (folder 03) shapes behavior <---+---> Scalable oversight keeps supervision
                                          |       working as models surpass humans
Interpretability (folder 06) lets us verify internally, not just behaviorally
Security & red teaming (folders 04, 05) stress-test against adversaries
```

Trustworthy AI isn't one technique — it's this **whole stack** working together,
with **measurement (evals)** as the connective tissue that turns hopes into
decisions.

---

## Hands-on ideas (`10-projects/`)

- **Build a small eval.** Pick one property (e.g. sycophancy, or refusal
  robustness), build a dataset, define scoring, run it on 2-3 open models, compare.
  Use a framework like **Inspect** (UK AISI) or **lm-evaluation-harness**, or roll
  your own. Designing a *good* eval is a deep skill labs value highly.
- **Reproduce a tiny weak-to-strong demo.** Train a strong model on labels from a
  weak model; measure whether it exceeds the weak teacher. Even a toy version
  teaches the core idea.

Designing rigorous evals is, honestly, one of the most *employable* skills in AI
safety right now — many roles are essentially "build trustworthy measurements."

---

## Check yourself

1. Why is it hard to *prove* a model lacks a dangerous capability?
2. What is Goodhart's law and how does it threaten benchmarks?
3. In one sentence, what is the scalable oversight problem?
4. Explain the bet behind AI Debate.
5. What does an RSP/ASL system actually gate, and on what evidence?

Next folder: [`../08-papers/reading-list.md`](../08-papers/reading-list.md)
