# Fellowship Prep: How to Actually Get In

This file is your strategy doc for AI safety research fellowships — the **Anthropic
Fellows Program** especially, plus strong alternatives. The single most important
sentence in this whole folder:

> **You get in by *doing visible research*, not by *credentials*.** Build a small
> body of real work and show your thinking. That's the whole game.

> ⚠️ Details (dates, stipend, structure, application format) **change every cohort.**
> Always verify the current specifics on anthropic.com and the program's page
> before applying. Treat the numbers below as "general shape," not gospel.

---

## What the Anthropic Fellows Program is (general shape)

- A **funded, mentored** program to help people transition into AI safety research.
- Roughly **~6 months, full-time**, with a **stipend** and **compute** provided.
- You're **paired with an Anthropic researcher** as a mentor and work on a real
  safety research project, often co-authoring a paper/output.
- Common focus areas: **interpretability, alignment/fine-tuning, evals/dangerous
  capabilities, AI security/red-teaming, scalable oversight.** (Maps directly onto
  this folder's structure — not a coincidence.)
- It's aimed at people with **strong technical/ML ability** who are newer to safety
  research specifically — i.e. you don't need to already be a safety researcher.

It is competitive, but it explicitly exists to bring in **new** people. That's you.

---

## What they actually screen for (and how to show each)

1. **Engineering / ML ability** — can you run real experiments and write code that
   works? → *Show:* a public GitHub with clean, reproducible reproductions and
   experiments (your `10-projects/` work).
2. **Research taste & reasoning** — can you pick good questions, design clean
   experiments, interpret results honestly, and reason about uncertainty? → *Show:*
   writeups with clear hypotheses, "what would change my mind," and honest negative
   results.
3. **Genuine safety motivation** — do you actually understand and care *why* this
   matters? → *Show:* engagement with the ideas (this folder!), a thoughtful "why
   safety" statement, references to specific papers/problems.
4. **Communication** — can you explain complex things clearly and be calibrated
   about what you do/don't know? → *Show:* a blog post or two; clear READMEs;
   honest framing.

Notice none of these is "have a PhD" or "have published before." They're all
*demonstrable by building things.*

---

## Your concrete portfolio plan (build over the 12-week roadmap)

Aim for **2-3 solid pieces**, each public (GitHub + a short writeup/blog):

1. **One paper reproduction.** Pick from this folder's projects: implement **DPO**
   (folder 03), find an **induction head** with TransformerLens (folder 06), or
   reproduce an **adversarial example / GCG-style** result (folder 04). Reproducing a
   known result *correctly* proves you can do real ML.

2. **One small original experiment.** Doesn't need to be novel-to-the-world — just
   *your own question*, cleanly tested. E.g. "how does jailbreak success rate change
   across 3 rephrasing styles on model X?" (folder 05), or "does feature Y from an
   SAE causally affect behavior Z?" (folder 06). **Negative results are fine** —
   honesty about them is a *plus*.

3. **One clear writeup / blog post.** Explain a safety concept or your experiment to
   a smart non-expert. Teaching reveals understanding (it's why this whole folder is
   written as teaching).

Quality bar: reproducible (someone can run it), documented (clear README), honest
(state limitations), and *thoughtful* (why it matters, what's next).

---

## The research proposal / statement (skeleton)

Many applications ask for research interests or a mini-proposal. Use this skeleton:

```markdown
- Question (1 sentence, specific & falsifiable):
- Why it matters for AI safety:
- Approach / experiment (what you'd actually run):
- What result would change your mind / what you'd learn either way:
- Prior work you build on (cite 2-3 papers):
- Why you're a good fit to do this (your relevant skills/projects):
```

Good proposals are **narrow, concrete, and honest** about uncertainty. A small
well-posed question beats a grand vague vision.

---

## Application timeline checklist

- [ ] Work through this folder (foundations → security → interp → evals).
- [ ] Do Karpathy's "Zero to Hero" + build nanoGPT.
- [ ] Ship reproduction project #1 (public).
- [ ] Read & summarize the 6 "minimal path" papers (folder 08).
- [ ] Ship original experiment #2 (public).
- [ ] Write blog post #3.
- [ ] Draft research statement; get feedback (post in a community, see below).
- [ ] Polish GitHub: pinned repos, clean READMEs, reproducible.
- [ ] Verify current application window/requirements on anthropic.com.
- [ ] Apply. Also apply to the alternatives below (don't single-thread).

---

## Strong alternatives (apply broadly — this is a portfolio of bets)

- **MATS (ML Alignment & Theory Scholars)** — premier mentorship program for new
  safety researchers; many paths into the field run through it. High priority.
- **Anthropic regular roles** — Research Engineer / Member of Technical Staff; the
  Fellows program is one door, not the only one.
- **ARENA** (Alignment Research Engineer Accelerator) — intensive upskilling
  bootcamp; excellent *before* fellowships.
- **Other labs/orgs:** Redwood Research, Apollo Research, UK AISI, EleutherAI (open
  collaboration), GoodFire, Transluce, and university safety groups.
- **AI safety camps / SPAR / open-source collabs** — lower-barrier ways to get a
  first project and a collaborator.

Treat applications like research: many small bets, learn from each, iterate.

---

## Where to plug into the community (do this early)

- **LessWrong / AI Alignment Forum** — where a lot of safety research is discussed
  and published; post your writeups there for feedback.
- **Mechanistic interpretability community** (Neel Nanda's resources, open Slacks/
  Discords) — welcoming to newcomers.
- **EleutherAI Discord** — open ML/safety collaboration.
- **Twitter/X** — many safety researchers share work and opportunities.

Getting feedback early and publicly is how you improve fast *and* get noticed.

---

## Mindset for applicants

- **Reproduce before you innovate.** Credibility comes from getting known results right.
- **Be honest, including about failure.** "This didn't work, here's my best guess
  why" is *exactly* the scientific maturity they want.
- **Narrow and deep beats broad and shallow.** One real result > ten half-ideas.
- **Consistency compounds.** A small project every few weeks builds an undeniable
  portfolio in months.
- **It's okay to be confused.** Everyone in this field is working at the edge of the
  unknown. Showing *how you reason through confusion* is the skill.

---

## Check yourself

1. What's the #1 thing that gets you into a fellowship (not credentials — what)?
2. What three portfolio pieces should you build, and what does each prove?
3. Why are negative results acceptable (even good) in your writeups?
4. Name two alternatives to apply to alongside Anthropic Fellows.

Next: start building. See [`../10-projects/README.md`](../10-projects/README.md).
