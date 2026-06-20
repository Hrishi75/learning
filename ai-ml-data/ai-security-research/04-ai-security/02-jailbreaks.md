# 02 — Jailbreaking (bypassing a model's safety training)

A **jailbreak** is an input that gets a model to do something its safety training
was supposed to prevent. Studying jailbreaks tells you *how robust a model's
safety actually is* — usually less than it looks. This file explains the
**categories and the why**, for defense and red-teaming purposes. It does **not**
provide working attack payloads — that's not what makes you a good researcher;
understanding *mechanisms and defenses* does.

---

## Jailbreak vs prompt injection (don't confuse them)

- **Prompt injection** (previous file): hijack the model's *task/instructions*,
  often via untrusted data, to make it act for an attacker. The target is the
  *application's control flow.*
- **Jailbreak:** get the model to violate its *safety/content rules* (produce
  disallowed content). The target is the *model's guardrails.*

They overlap (an injection can carry a jailbreak), but the intent differs: injection
= "do my task instead"; jailbreak = "break your own rules."

---

## Why do jailbreaks work at all? (the mechanism)

Safety training (RLHF/CAI from folder 03) doesn't install a hard rule engine. It
**shifts probabilities**: it makes refusals more likely for harmful-looking
requests. But the underlying model still *contains* the capability and can be
nudged back toward it. Jailbreaks exploit gaps in that probabilistic shield:

1. **Safety is shallow / pattern-matched.** Training covers the harmful requests it
   *saw*, phrased the ways it saw them. Reword, reframe, or encode the request and
   it may fall outside the trained "refuse" region. The model never learned a deep,
   general concept of "harmful" — it learned correlations.

2. **Helpfulness vs harmlessness tension.** The model is trained to be both helpful
   and harmless (folder 03). Attacks manufacture a frame where being "helpful"
   seems to win — e.g. an appeal to a fictional, academic, or hypothetical context
   — so the helpful drive overrides the cautious one.

3. **Distribution shift.** Anything far from the training distribution (weird
   formats, other languages, long elaborate setups, unusual encodings) lands in
   under-defended territory.

> Researcher's takeaway: jailbreaks are evidence that current safety is a *patch on
> the surface*, not a property of the model's core understanding. Closing that gap
> is open research — and connects to interpretability (folder 06: can we find and
> strengthen the actual "refuse harmful" mechanism inside the weights?).

---

## Categories of jailbreaks (conceptual taxonomy)

Know the *families* and *why each works*. (Descriptions are high-level on purpose.)

1. **Role-play / persona framing.** Convince the model it's playing a character or
   alternate system without the rules. Works by exploiting the model's strong
   instruction-following and story-completion drive.

2. **Hypothetical / fictional wrappers.** Embed the request in "for a novel,"
   "in a purely academic sense," "as a thought experiment." Exploits the
   helpful-in-context frame and the model's difficulty distinguishing a real
   request from a framed one.

3. **Many-shot / long-context jailbreaking** (notable Anthropic finding). Fill a
   long context with many fake examples of the model *complying* with harmful
   requests; the model then continues the pattern on a final real request. This
   exploits **in-context learning** — the model imitates patterns it sees in
   context — and got more effective as context windows grew. Anthropic published
   this specifically to drive defenses. (See folder 08.)

4. **Multi-turn / gradual escalation ("crescendo").** Start benign, then nudge
   step by step across many turns until you're somewhere the model would've
   refused in one shot. Exploits the lack of a global "where is this conversation
   heading?" check.

5. **Obfuscation / encoding.** Express the request in another language, in code,
   in ciphers, with odd spacing/unicode, etc., so safety pattern-matching (which is
   strongest in plain English) misses it — but the capable model still understands.
   Ties directly to the **tokenization** gap (folder 02-00).

6. **Optimization-based / automated attacks.** Use algorithms to *search* for an
   input that breaks the model — e.g. **GCG** (Greedy Coordinate Gradient, Zou et
   al. 2023) finds an adversarial *suffix* string by gradient search. Notably, such
   suffixes can **transfer** across different models. This blurs into "adversarial
   examples" (next file) and shows safety can be broken *systematically*, not just
   by clever wording.

---

## Defenses (the part that matters)

Like injection, defense is layered and imperfect:

1. **Better/broader safety training.** Train on diverse paraphrases, languages, and
   known jailbreak patterns (adversarial training). Helps, but it's whack-a-mole —
   new attacks keep appearing.

2. **Input & output classifiers ("guardrail models").** A separate model screens
   the request and the response for harmful content, independent of the main
   model's mood. Anthropic's **Constitutional Classifiers** work is an example of
   robust output-screening that dramatically reduced jailbreak success in testing.

3. **Context monitoring for multi-turn attacks.** Track the *trajectory* of a
   conversation, not just the last message, to catch crescendo-style escalation.

4. **Limiting context-based exploits.** Detecting/limiting many-shot patterns,
   capping how much untrusted in-context "demonstration" can steer behavior.

5. **Interpretability-based detection** (folder 06). If you can identify the
   internal "feature" that represents a harmful intent or a deception, you can
   monitor or clamp it. Early but promising.

6. **Defense-in-depth around the model.** Even if a jailbreak succeeds, limit what
   the *system* can do with the output (don't auto-execute, sandbox tools) — same
   least-privilege idea as injection.

---

## The research framing (how to think like Anthropic about this)

Don't think "how do I jailbreak X." Think:
- **"How do I *measure* a model's robustness to a whole class of attacks?"**
  (build a benchmark / eval)
- **"Why does this class work — what internal mechanism is it exploiting?"**
  (interpretability)
- **"What defense reduces success rate across many attack types without
  over-refusing benign requests?"** (the real, hard tradeoff)

That last point is key: a model that refuses *everything* is "safe" and useless.
The art is robustness to attacks **while staying helpful** on legitimate requests.
Measuring both at once is exactly the kind of rigorous work fellowships reward.

---

## Ethics (non-negotiable)

- Study jailbreaks to **build defenses and evals**, on **open/local models** or
  authorized test systems.
- **Responsible disclosure**: report novel jailbreaks of real systems privately to
  the vendor (many run bug-bounty / model-safety reporting programs).
- Never use jailbreaks to actually obtain genuinely harmful content. The goal is a
  *safer* system, and that intent is what distinguishes a researcher from an
  attacker.

---

## Hands-on idea (`10-projects/`)

Build a **mini jailbreak-robustness eval** on a small open model:
1. Collect a set of benign requests and a set of clearly-disallowed requests.
2. Apply a few *categories* of transformation (e.g. translate, reframe as
   hypothetical) to the disallowed set.
3. Measure: refusal rate on plain vs transformed; over-refusal rate on benign.
4. Add a simple output classifier and re-measure.
5. Report the tradeoff curve. That's a real, presentable result.

---

## Check yourself

1. How is a jailbreak different from a prompt injection?
2. Give the deep reason jailbreaks are possible (what is safety training, really?).
3. Why did many-shot jailbreaking become *more* effective over time?
4. Why is "refuse everything" not a valid defense?

Next: [`03-adversarial-and-poisoning.md`](03-adversarial-and-poisoning.md)
