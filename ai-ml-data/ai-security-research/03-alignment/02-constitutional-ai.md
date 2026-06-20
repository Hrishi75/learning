# 02 — Constitutional AI (Anthropic's signature alignment method)

If you're aiming at Anthropic specifically, understand this one well — it's their
flagship alignment technique, introduced in the 2022 paper *"Constitutional AI:
Harmlessness from AI Feedback."* It's also a beautiful idea.

---

## The problem it solves

Standard RLHF (previous file) needs **humans** to label which responses are
harmful. Problems with that:
1. **Slow and expensive** — humans are a bottleneck.
2. **Psychologically harmful** — labelers must read disturbing content to flag it.
3. **Inconsistent and opaque** — different humans disagree; the "values" live in
   thousands of individual judgments, not anywhere you can read and debate.

Constitutional AI (CAI) asks: *what if the AI could supervise its own harmlessness
using a written set of principles — a "constitution" — instead of constant human
labeling?*

---

## The core idea: the model critiques and revises itself

CAI uses the model to improve itself against explicit written principles. Two
phases:

### Phase 1 — Supervised stage (self-critique and revision)
1. Prompt the model with something potentially harmful.
2. It produces a first (possibly bad) response.
3. Ask the *same* model to **critique** its own response against a principle from
   the constitution:
   > "Identify ways your last response was harmful, unethical, or dangerous."
4. Ask it to **revise** the response to fix those problems.
5. Keep the improved (revised) response as training data.
6. Fine-tune the model on these self-revised, better answers.

```
harmful prompt
   -> model's first answer (maybe bad)
   -> model critiques it against a written principle
   -> model rewrites it to be better
   -> use the rewrite as training data
```

The model literally teaches itself to be more harmless by repeatedly catching and
fixing its own mistakes, guided by principles.

### Phase 2 — RL stage (RLAIF: RL from AI Feedback)
Like RLHF's preference step, but the **AI** does the comparing instead of humans:
1. Generate two responses to a prompt.
2. Ask the model: "Which response better follows [principle]?" — the AI picks.
3. Use those AI-generated preferences to train a reward model.
4. Optimize the LLM against it (same RL machinery as RLHF).

So RLHF's "human feedback" becomes "AI feedback guided by a constitution" =
**RLAIF**. Humans still write the constitution and oversee the process, but they
no longer label every individual example.

---

## What is "the constitution"?

A short list of written **principles** the model should follow. Examples in the
spirit of Anthropic's published one:

- "Choose the response that is least harmful, unethical, or deceptive."
- "Choose the response that most discourages illegal, dangerous, or unethical activity."
- "Choose the response that is most helpful, honest, and harmless."
- Principles drawn from sources like the UN Declaration of Human Rights, trust &
  safety best practices, etc.

Why this is powerful for safety:
- **Transparency:** the values are *written down* and can be read, debated, and
  revised — not buried in millions of opaque human labels.
- **Scalability:** the AI can apply principles to far more examples than humans could.
- **Adjustability:** change a principle, re-run — you can study how values map to behavior.

> Big-picture significance: it's a step toward **making a model's values explicit
> and editable**, rather than an emergent mystery. That aligns with the whole
> interpretability/transparency philosophy at Anthropic.

---

## CAI vs RLHF (quick compare)

| | RLHF | Constitutional AI (CAI) |
|---|---|---|
| Who judges harmfulness? | Humans label each example | AI judges, guided by written principles |
| Values stored as... | Many opaque human labels | An explicit, readable constitution |
| Human cost | High (label everything) | Lower (write principles, oversee) |
| Labeler harm exposure | High | Much lower |
| Transparency of values | Low | Higher |

CAI doesn't *replace* human input — humans write the constitution and still do
helpfulness feedback. It shifts *harmlessness* supervision to be principle-driven
and AI-assisted.

---

## Honest caveats (good researchers note these)

- The model judging itself can inherit its **own blind spots and biases** — if it
  misunderstands a principle, it scales that mistake.
- Writing a good constitution is hard; principles can conflict or be gamed.
- "The AI supervises the AI" raises a chicken-and-egg worry: can a flawed model
  reliably correct itself? (This connects to **scalable oversight**, folder 07,
  and ideas like weak-to-strong generalization.)
- Anthropic later explored **Collective Constitutional AI** — involving the public
  in choosing principles — to address "whose values?" 

These open problems are exactly the kind of thing a fellowship application could
engage with thoughtfully.

---

## Connection to the rest of this folder

- Builds directly on RLHF (previous file) — same RL machinery, different feedback source.
- It's an early example of **scalable oversight** (folder 07): using AI to help
  supervise AI.
- Its emphasis on *explicit, inspectable values* rhymes with **interpretability**
  (folder 06): both want to make the model's behavior legible, not magical.

---

## Check yourself

1. What two problems with human-labeled RLHF does CAI address?
2. Describe the critique-and-revise loop in your own words.
3. What does "RLAIF" mean, and how does it differ from RLHF?
4. Give one genuine weakness of CAI.

Read the paper next (folder 08 reading list): *Constitutional AI: Harmlessness
from AI Feedback* (Bai et al., 2022).

Next folder: [`../04-ai-security/00-overview.md`](../04-ai-security/00-overview.md)
