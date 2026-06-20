# Reading List — The Papers That Matter (with a summary system)

You don't read papers like novels. You read them **actively**, in passes, and you
**write a summary** for each. This file gives you (1) a reading method, (2) a
curated list ordered for a beginner, and (3) a copy-paste summary template.

> Rule: don't just collect papers — *finish and summarize* them. One paper deeply
> understood beats ten skimmed. Move each from `[ ]` to `[done]` only after you've
> written its summary below.

---

## How to read a research paper (the 3-pass method)

**Pass 1 (5-10 min): Is this worth my time / what's the claim?**
Read title, abstract, intro, figures, and conclusion only. Answer: what problem,
what's the main claim, what's the result? Stop here if it's not relevant.

**Pass 2 (~1 hr): Understand the idea.** Read the whole thing, but skip heavy proofs.
Focus on the method and the experiments. Note terms you don't know (look them up or
add to [`../glossary.md`](../glossary.md)). Sketch the method in your own words.

**Pass 3 (deep, optional): Could I reproduce it?** Read every detail, re-derive key
steps, mentally (or actually) re-implement. Do this only for papers you want to
build on.

For most papers, passes 1-2 + a written summary are enough. Reserve pass 3 for the
2-3 papers you'll reproduce as projects.

---

## Tips
- **Start with blog posts / distillations** when they exist (Anthropic, OpenAI, and
  many authors write accessible versions). Then read the paper.
- Use tools: **alphaXiv**, **arXiv**, Connected Papers (to see related work), and
  ask an LLM to explain a confusing paragraph (then verify against the paper).
- Keep a running list of **open questions** each paper raises — that's where your
  *own* research ideas come from.

---

## The curated list (ordered for a beginner)

Legend: `[ ]` todo · `[r]` read+summarized · `[x]` reproduced. Difficulty: ⭐ easy
intuition exists · ⭐⭐ moderate · ⭐⭐⭐ hard.

### Tier 1 — Foundations of LLMs (read first)
- [ ] ⭐⭐ **Attention Is All You Need** (Vaswani et al., 2017) — introduces the
  Transformer. Pair with Karpathy's videos + "The Illustrated Transformer" blog.
- [ ] ⭐ **Language Models are Few-Shot Learners — GPT-3** (Brown et al., 2020) —
  scale + in-context learning. Skim the experiments.
- [ ] ⭐⭐ **Scaling Laws for Neural Language Models** (Kaplan et al., 2020) — why
  bigger is predictably better.
- [ ] ⭐⭐ **Training Compute-Optimal LLMs — "Chinchilla"** (Hoffmann et al., 2022) —
  the data/size correction to scaling laws.

### Tier 2 — Alignment (the core of safety practice)
- [ ] ⭐⭐ **Training LMs to follow instructions with human feedback — "InstructGPT"**
  (Ouyang et al., 2022) — the canonical RLHF paper.
- [ ] ⭐⭐ **Constitutional AI: Harmlessness from AI Feedback** (Bai et al., 2022,
  Anthropic) — *read this one carefully if targeting Anthropic.*
- [ ] ⭐⭐ **Direct Preference Optimization (DPO)** (Rafailov et al., 2023) — the
  simpler RLHF alternative you can implement.
- [ ] ⭐ **Red Teaming Language Models to Reduce Harms** (Ganguli et al., 2022,
  Anthropic) — how labs find harms at scale.

### Tier 3 — AI security & attacks
- [ ] ⭐⭐ **Universal and Transferable Adversarial Attacks on Aligned LMs — "GCG"**
  (Zou et al., 2023) — automated jailbreak suffixes that transfer.
- [ ] ⭐ **Many-shot Jailbreaking** (Anthropic, 2024) — long-context attack; very
  readable.
- [ ] ⭐⭐ **Sleeper Agents: Training Deceptive LLMs that Persist Through Safety
  Training** (Hubinger et al., 2024, Anthropic) — *must-read*; deception + backdoors.
- [ ] ⭐⭐ **Not what you've signed up for: Compromising real-world LLM apps with
  indirect prompt injection** (Greshake et al., 2023) — the indirect-injection paper.

### Tier 4 — Interpretability
- [ ] ⭐⭐⭐ **A Mathematical Framework for Transformer Circuits** (Elhage et al., 2021,
  Anthropic) — dense; read the blog/walkthroughs alongside.
- [ ] ⭐⭐ **In-context Learning and Induction Heads** (Olsson et al., 2022, Anthropic).
- [ ] ⭐⭐ **Toy Models of Superposition** (Elhage et al., 2022, Anthropic) — why
  neurons are polysemantic.
- [ ] ⭐⭐ **Towards Monosemanticity: Decomposing Language Models With Dictionary
  Learning** (Bricken et al., 2023, Anthropic) — SAEs introduced.
- [ ] ⭐⭐ **Scaling Monosemanticity** (Templeton et al., 2024, Anthropic) — SAEs on
  Claude 3 Sonnet; "Golden Gate" features.

### Tier 5 — Oversight, evals & governance
- [ ] ⭐⭐ **AI Safety via Debate** (Irving et al., 2018).
- [ ] ⭐⭐ **Weak-to-Strong Generalization** (Burns et al., 2023, OpenAI).
- [ ] ⭐ **Anthropic Responsible Scaling Policy (RSP)** — read the current version on
  anthropic.com (it's a policy doc, not arXiv; updated over time).
- [ ] ⭐ A recent **frontier dangerous-capability evaluation** report (pick a current
  one from Anthropic / UK AISI / a model card).

### Background / orientation (read any time, very accessible)
- [ ] ⭐ **"Concrete Problems in AI Safety"** (Amodei et al., 2016) — the classic
  problem-framing paper; still a great mental map.
- [ ] ⭐ **Anthropic "Core Views on AI Safety"** (blog) — understand the lab's worldview.
- [ ] ⭐ **Neel Nanda — "200 Concrete Open Problems in Mechanistic Interpretability"**
  — your project idea mine.

---

## Summary template (COPY this block per paper)

Create one file per paper here in `08-papers/` (e.g. `dpo.md`) using this:

```markdown
# <Title> (<first author> et al., <year>)

- **Link:** <arxiv/blog url>
- **One-line claim:** <the single main result in plain English>
- **Problem:** <what gap/question it addresses>
- **Method:** <how they did it, in your own words — 3-5 sentences>
- **Key result(s):** <the numbers/findings that matter>
- **Why it matters for safety:** <the safety relevance>
- **Strengths:** <what's convincing>
- **Limitations / what I doubt:** <be critical — this is the researcher muscle>
- **Open questions it raises (MY ideas):** <future work — your research seeds>
- **Terms I learned:** <add to ../glossary.md>
```

That "Limitations" + "Open questions" habit is what turns a reader into a
researcher. Fellowships look for people who can *critique* and *extend* work, not
just summarize it.

---

## Suggested order if overwhelmed

If the list feels like a lot, do exactly this minimal path first, in order:
1. Karpathy videos (not a paper, but do them) →
2. Attention Is All You Need →
3. InstructGPT →
4. Constitutional AI →
5. Sleeper Agents →
6. Towards Monosemanticity.

Those six give you a coherent arc: how LLMs work → how we align them → how that
fails → how we might look inside. Everything else extends this spine.
