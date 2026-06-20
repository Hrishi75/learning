# 00 — AI Security: The Threat Landscape (overview)

"AI security" = protecting AI systems from people who want to **trick, corrupt,
steal, or misuse** them. It overlaps with alignment (folder 03) but the framing is
different: alignment asks "does the model pursue the right goal?"; security asks
"can an **adversary** make the model misbehave?"

This file is the map. The next files go deep on each major attack. Everything here
is taught for **defense and research** — understanding attacks is how you build
defenses, run red teams, and pass security reviews. That's the same reason
universities teach how locks get picked.

---

## A simple way to organize AI attacks

Attacks target different stages of an AI system's life. Use this mental table:

| When | Attack family | One-line description | Deep-dive file |
|------|---------------|----------------------|----------------|
| **At inference** (you talk to the model) | **Prompt injection** | Sneak instructions into the model's input to hijack it | [`01-prompt-injection.md`](01-prompt-injection.md) |
| At inference | **Jailbreaking** | Get the model to bypass its own safety rules | [`02-jailbreaks.md`](02-jailbreaks.md) |
| At inference | **Adversarial examples** | Tiny crafted input changes that cause big wrong outputs | [`03-adversarial-and-poisoning.md`](03-adversarial-and-poisoning.md) |
| **At training** | **Data poisoning / backdoors** | Corrupt training data to plant hidden behavior | [`03-adversarial-and-poisoning.md`](03-adversarial-and-poisoning.md) |
| **Against the model asset** | **Model extraction / stealing** | Copy a model's behavior or weights by querying it | this file (below) |
| **Against privacy** | **Membership inference / data extraction** | Pull private training data back out of the model | this file (below) |

Memorize the three "when"s: **training time, inference time, and the model
itself.** Every attack hits one of those.

---

## Why LLMs created a whole new security problem

Traditional software has a clean line between **code** (instructions) and **data**
(stuff to process). Your text editor never "runs" the novel you type into it.

**LLMs erased that line.** To an LLM, *everything is text in the same context
window* — your instructions, the user's data, a webpage it's reading, a tool's
output. The model can't fundamentally tell "trusted instruction from my developer"
apart from "untrusted text from a malicious website." They're all just tokens it
attends over (remember folder 02 — attention treats the whole context together).

> This single fact — **LLMs don't reliably separate instructions from data** — is
> the root cause of prompt injection, the #1 unsolved LLM security problem. Hold
> onto it; it'll appear in every file in this folder.

---

## Quick tour of the major attacks (full files follow)

### 1. Prompt injection
An attacker plants instructions in content the model will read, hijacking its
behavior. *Direct:* the user types malicious instructions. *Indirect:* the
malicious instructions hide in external data the model fetches (an email, a
webpage, a PDF) — far more dangerous because the victim didn't write them. Critical
once LLMs have **tools** (send email, browse, run code), because a hijack can take
real actions. → [`01-prompt-injection.md`](01-prompt-injection.md)

### 2. Jailbreaking
Tricking the model into ignoring its safety training to produce content it's
supposed to refuse. Techniques: role-play framings, hypothetical wrappers, slow
escalation, very long contexts, encodings. Studying *why* jailbreaks work reveals
how shallow or robust the model's safety really is. → [`02-jailbreaks.md`](02-jailbreaks.md)

### 3. Adversarial examples
Tiny, often human-invisible changes to an input that flip the model's output.
Classic in image models (change a few pixels, "panda" becomes "gibbon"); in LLMs,
optimized "suffix" strings can break alignment. Reveals models rely on fragile
patterns, not robust understanding. → [`03-adversarial-and-poisoning.md`](03-adversarial-and-poisoning.md)

### 4. Data poisoning & backdoors
Corrupt the *training* data so the model learns a hidden, attacker-chosen behavior
that triggers on a secret signal — while behaving normally otherwise. Scary because
training data comes from the open web, which anyone can edit.
→ [`03-adversarial-and-poisoning.md`](03-adversarial-and-poisoning.md)

### 5. Model extraction / stealing
By querying a model a lot and studying its outputs, an attacker can train a copy
("distill" it) — stealing the expensive product — or even recover some weights via
clever API probing. Threatens both IP and safety (a stolen model has no guardrails
you control).

### 6. Privacy attacks (membership inference & data extraction)
- **Membership inference:** figure out whether a specific record was in the
  training data (e.g. "was *this person's* medical note used?"). A privacy leak.
- **Training data extraction:** prompt the model so it regurgitates memorized
  training data verbatim — which can include secrets, personal info, or copyrighted
  text. Big models memorize more than you'd expect.

---

## How defenders respond (the other half of the field)

For every attack, there's defensive research. You'll want to understand both:

- **Input/output filtering:** classifiers that screen prompts and responses for
  attacks or harmful content (imperfect — attackers adapt).
- **Instruction hierarchy / privilege separation:** teach the model to trust
  system/developer instructions over user/data instructions (an active research
  direction; not fully solved).
- **Adversarial training:** train the model on attack examples so it's more robust.
- **Sandboxing & least privilege:** limit what tools/actions the model can take, so
  a successful hijack does less damage (classic security principle applied to AI).
- **Red teaming & evals:** systematically hunt for failures before attackers do
  (folders 05, 07).
- **Interpretability-based defenses:** detect attacks by reading the model's
  internals (folder 06) — e.g. spotting a "deception" feature lighting up.

The honest state of the art: **none of these fully solve the problems.** AI
security is wide open — which is exactly why it's a great research area for you.

---

## Ethics & rules of engagement (read this, it matters for fellowships)

You will study attacks. Do it responsibly:
- **Only test systems you own or are authorized to test.** Same rule as all
  security work.
- **Use open models locally** for hands-on experiments (e.g. small HuggingFace
  models) rather than attacking live production services.
- **Practice responsible disclosure:** if you find a real vulnerability, report it
  privately to the vendor before publishing.
- **Frame your work as defense.** Fellowships and security teams value people who
  find problems *in order to fix them.* That mindset is your credential.

---

## Connection to the bigger picture

AI security and alignment are two sides of trustworthy AI: alignment makes the
model *want* the right thing; security stops *adversaries* from overriding that.
As models get tools and autonomy, security stops being about "bad text output" and
becomes about "bad actions in the real world" — which is why this field is
exploding right now.

---

## Check yourself

1. What's the root cause that makes prompt injection possible (one sentence)?
2. Name the three "when"s that all attacks target.
3. What's the difference between direct and indirect prompt injection?
4. Why does giving an LLM tools make security much more serious?

Next: [`01-prompt-injection.md`](01-prompt-injection.md)
