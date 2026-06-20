# 00 — Red Teaming: Systematically Finding a Model's Failures

**Red teaming** = deliberately attacking your own system to find its weaknesses
*before* real adversaries (or accidents) do. The term comes from military/security
practice: the "red team" plays the attacker; the "blue team" defends. For AI, red
teaming is how labs discover harmful behaviors, jailbreaks, and failure modes
ahead of deployment. Anthropic, OpenAI, and others red-team every major model
release.

---

## Why red teaming is its own discipline (not just "try some attacks")

Anyone can poke a model once. Red teaming is the **systematic, measured** version:
- coverage (test *many categories* of harm, not your favorites),
- reproducibility (record exactly what you did so others can verify),
- measurement (how *often* does it fail, not just "it failed once"),
- and feedback into fixes (findings must improve the model/system).

It's the empirical, hands-on counterpart to the theoretical alignment work in
folder 03. If alignment asks "how should the model behave?", red teaming asks
"let's go *find out* where it doesn't."

---

## The two main styles

### 1. Manual (human) red teaming
Skilled humans creatively try to make the model misbehave: harmful content,
privacy leaks, biased outputs, jailbreaks (folder 04), tool-misuse in agents.
- **Strengths:** creative, finds surprising/novel failures, good judgment on
  what's actually harmful.
- **Weaknesses:** slow, expensive, can't cover everything, and exposes humans to
  disturbing content.

Anthropic's 2022 paper *"Red Teaming Language Models to Reduce Harms"* documents
doing this at scale and releasing the dataset — a great read (folder 08).

### 2. Automated red teaming
Use *another model* (or an algorithm) to generate large numbers of attack attempts
automatically. E.g., a "red-team LLM" is tasked with writing prompts that make the
target model fail; successful attacks are collected and used to train the target to
be safer.
- **Strengths:** scale (millions of attempts), cheap, runs continuously, no human
  trauma.
- **Weaknesses:** the attacker model has blind spots too; may miss the creative,
  out-of-distribution attacks humans find.

Best practice combines both: humans for creativity and judgment, automation for
coverage and scale. This human+AI loop is itself a research topic.

---

## A practical red-teaming process (use this structure)

A clean methodology you can actually apply (and describe in an application):

1. **Define scope & threat model.** What are you testing for? (e.g. "will the agent
   leak data via indirect injection?" or "does it produce disallowed content under
   reframing?") Be specific. You can't test "is it safe" — too vague.

2. **Enumerate harm categories.** Build a checklist (e.g. dangerous instructions,
   privacy, bias/fairness, misinformation, security/tool-misuse, over-refusal).
   Coverage matters.

3. **Generate attack attempts.** Manual + automated, across categories and across
   *transformations* (rephrasings, languages, encodings, multi-turn). Vary
   systematically, not randomly.

4. **Define success criteria.** Decide *in advance* what counts as a failure, so you
   judge consistently. Ideally use a rubric or a classifier so it's reproducible.

5. **Measure rates.** Report **attack success rate** per category, not anecdotes.
   "Reframing jailbreaks succeeded 23% of the time on category X" is a result;
   "I got it to say a bad thing once" is not.

6. **Also measure over-refusal.** Test benign-but-sensitive prompts to ensure your
   safety isn't just refusing everything. The helpful/harmless tradeoff (folder 03)
   must be measured from *both* sides.

7. **Report & feed back.** Document reproducibly; propose/test mitigations; re-run
   to show improvement. The loop closes here.

> This 7-step structure *is* an experimental design. Running even a small version
> of it well is more impressive to a fellowship than a flashy one-off jailbreak.

---

## Key metrics to know

- **Attack Success Rate (ASR):** fraction of attack attempts that succeed. The
  headline number.
- **Over-refusal / false-refusal rate:** fraction of *benign* requests wrongly
  refused. The cost of safety.
- **Robustness:** how ASR holds up across attack *categories* and *transformations*
  (not just one).
- **Severity-weighting:** not all failures are equal; a data-exfiltration is worse
  than a mild policy slip. Weight accordingly.

Good red teaming reports a **tradeoff**, not a single number: safety vs.
helpfulness, like an ROC curve.

---

## How this connects to the rest

- Red teaming is where folder 04's **attacks** become **measurements.**
- Its results feed **alignment** (folder 03): failures become training data
  (adversarial training, RLHF examples).
- It overlaps heavily with **evals** (folder 07): red teaming for *dangerous
  capabilities* (bio, cyber, autonomy) is a special, high-stakes case tied to
  Responsible Scaling Policies.
- Findings motivate **interpretability** (folder 06): *why* did it fail internally?

---

## Hands-on idea (`10-projects/`)

Run a **mini structured red-team** on a small open model:
1. Pick ONE narrow scope (e.g. "robustness of refusals to 3 rephrasing styles").
2. Build a small labeled prompt set (benign + disallowed).
3. Apply your transformations, define a success rubric, measure ASR + over-refusal.
4. Produce a short report with a table and a chart.

It's small, honest, reproducible, and demonstrates exactly the empirical mindset
labs want. Pair it with the jailbreak/injection projects from folder 04.

---

## Ethics

Same rules as folder 04: authorized/own/open systems only; responsible disclosure
for real findings; the purpose is **to fix, not to exploit.** Document that intent
explicitly in any writeup.

---

## Check yourself

1. Why is red teaming "systematic," not just "trying attacks"?
2. Contrast manual vs automated red teaming — strengths of each.
3. Why must you measure over-refusal alongside attack success rate?
4. What's the difference between "I jailbroke it once" and a red-team *result*?

Next folder: [`../06-interpretability/00-mech-interp.md`](../06-interpretability/00-mech-interp.md)
