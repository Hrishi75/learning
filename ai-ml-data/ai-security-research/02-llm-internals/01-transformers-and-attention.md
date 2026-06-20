# 01 — The Transformer and Attention (the engine of every LLM)

This is the heart of the whole field. Every modern LLM — Claude, GPT, Gemini,
Llama — is a **Transformer**. The 2017 paper that introduced it is literally
titled "Attention Is All You Need." If you understand attention, you understand
the core of LLMs. We'll build the intuition slowly, no scary math.

---

## The problem the Transformer solves

To predict the next word, a model must understand how words *relate* across a
sentence. Consider:

> "The **animal** didn't cross the street because **it** was too tired."

What does "it" refer to? The animal. Now change one word:

> "The animal didn't cross the **street** because **it** was too wide."

Now "it" refers to the street. To get this right, when the model processes the
word "it", it must **look back** at the other words and figure out which one "it"
depends on. That looking-back-and-weighing is exactly what **attention** does.

---

## Attention in one sentence

> **Attention lets each word gather information from the other words that are
> most relevant to it, by computing similarity scores between them.**

That's it. The rest is mechanics. Let's unpack with an analogy, then the
Query/Key/Value idea.

---

## The library analogy (Query, Key, Value)

Imagine each word is a person in a library trying to understand itself better by
asking the other words for help.

- Every word writes a **Query**: "Here's what I'm looking for."
  (The word "it" asks: "I'm a pronoun — which noun am I?")
- Every word also holds up a **Key**: "Here's what I'm about."
  (The word "animal" advertises: "I'm an animal, a noun, a subject.")
- And every word has a **Value**: the actual information it will hand over if chosen.

The process:
1. Word "it" compares its **Query** against every other word's **Key** using a
   **dot product** (remember: dot product = similarity!).
2. High similarity = "you're relevant to me." "it"'s query matches "animal"'s key strongly.
3. Turn those similarity scores into weights with **softmax** (so they sum to 1).
4. Take a weighted blend of everyone's **Value**, weighted by relevance.
5. "it" now carries information mostly from "animal." It has *contextualized* itself.

So each word's new representation = a smart mix of all words, weighted by how
relevant each is. Do this for every word simultaneously.

```
For each word:
  scores   = dot(my Query, every Key)      # how relevant is each other word to me?
  weights  = softmax(scores)               # turn into 0..1 weights summing to 1
  output   = sum(weights * Values)         # weighted blend of information
```

---

## Where do Query, Key, Value come from?

Each word starts as an embedding vector (from the tokenization file). The model
multiplies that embedding by three learned weight matrices — `W_Q`, `W_K`, `W_V`
— to produce its Query, Key, and Value vectors. Those three matrices are part of
what the model *learns* during training. Different matrices = the model learns
*what* to pay attention to.

```
Query = embedding @ W_Q
Key   = embedding @ W_K
Value = embedding @ W_V
```

This is why attention is "learned": the model discovers, through training, the
W_Q/W_K/W_V that make relevant words light up for each other.

---

## "Self-attention" and "multi-head" attention

- **Self-attention** = the words are attending to *each other* in the same
  sentence (as above). "Self" because the queries and keys come from the same sequence.

- **Multi-head attention** = run several attention operations in *parallel*, each
  with its own W_Q/W_K/W_V. Why? Because a word relates to others in many ways at
  once. One "head" might track grammar (subject-verb), another might track meaning
  (which noun a pronoun refers to), another might track position. Each head learns
  a different *kind* of relationship. Their outputs are combined. Typical models
  have many heads (e.g. 12, 32, 96).

> Mental model: multi-head attention is like reading a sentence with several
> highlighters at once — one for grammar, one for references, one for tone — then
> merging what each highlighter found.

---

## The full Transformer block

Attention is the star, but a Transformer "block" wraps it with a few helpers.
Stack many of these blocks (e.g. 12, 32, or 100+) and you have an LLM.

```
input embeddings
      |
      v
┌──────────────────────────┐
│  1. Multi-head attention │   <- words exchange information
│  + residual + layernorm  │
├──────────────────────────┤
│  2. Feed-forward network │   <- each word "thinks" on its own
│  + residual + layernorm  │
└──────────────────────────┘
      |
      v   (repeat this whole block N times)
      v
  output -> predict next token
```

The two helper ideas, briefly:

- **Feed-forward network (FFN/MLP):** after words share info via attention, each
  word passes through a small neural net (like folder 01!) to process what it
  gathered. Intuition: attention is "talk to your neighbors," FFN is "go think
  about it alone." A LOT of the model's knowledge is stored here.

- **Residual connections ("+"):** add the block's input back to its output. This
  is a shortcut that lets information and gradients flow through very deep stacks
  without getting lost. Without residuals, deep networks barely train. (You'll
  meet residuals again in interpretability — the "residual stream" is where all
  the model's information lives.)

- **Layer normalization:** keeps the numbers in a healthy range so training stays
  stable. A practical stabilizer, not a deep idea — don't stress about it early.

---

## The "causal mask" — why an LLM can't peek ahead

When training an LLM to predict the next word, we must stop it from cheating by
looking at future words. So attention is **masked**: when processing word #5, it
can attend to words 1-5 but **not** 6, 7, 8... This is called **causal** (or
**autoregressive**) attention. It's why generation goes left-to-right, one token
at a time, each new token added to the context for the next.

```
predicting ->  The   cat   sat   on    ___
sees:          The   cat   sat   on          (never the future)
```

---

## Putting it ALL together: how an LLM generates text

Now you can read the whole pipeline end to end:

```
1. Your text  ->  tokens  ->  token IDs  ->  embeddings        (folder 02-00)
2. Add "position" info so the model knows word order
3. Pass through N Transformer blocks:
      - attention: words share relevant info
      - FFN: each word processes it
      - (repeat N times, deeper = richer understanding)
4. Final layer outputs a score (logit) for EVERY token in the vocabulary
5. Softmax -> probabilities over the whole vocabulary
6. Pick a token (highest prob, or sample with temperature)
7. Append it to the text, go back to step 1, repeat
```

Generating a paragraph = running this loop once per token. Claude writing you a
reply is doing exactly this, hundreds of times, very fast.

---

## Do the hands-on version: nanoGPT

Reading this gives intuition; *building* gives understanding. Do **Andrej
Karpathy's "Let's build GPT from scratch"** (YouTube) and his **nanoGPT** repo.
In ~300 lines you implement everything above and train a tiny GPT that generates
Shakespeare-like text on your laptop. After folder 01's from-scratch net, this is
the perfect next build. Put your version in `10-projects/`.

---

## Connection to AI safety (very important)

1. **Attention is interpretable-ish.** Because attention produces explicit
   weights ("word X looked 80% at word Y"), researchers can sometimes *read* what
   the model is doing. This is a foothold for **interpretability** (folder 06).
   Some attention heads do clean, human-understandable jobs (e.g. "induction
   heads" that copy patterns — you'll meet them later).

2. **Context = attack surface.** Since the model attends over *everything* in its
   context window equally (including text it didn't get from you — like a webpage
   it's reading), an attacker can plant instructions in that context. The model
   may "attend" to malicious instructions as if they were legitimate. That's
   **prompt injection** (folder 04).

3. **Scale brings surprises.** Stacking more blocks + more data produces abilities
   that weren't explicitly programmed (**emergent capabilities**). We can't fully
   predict what a bigger model will be able to do — which is precisely why safety
   research and evaluations (folder 07) matter before deployment.

---

## Check yourself

1. Explain Query, Key, Value using the library analogy.
2. Why is the dot product the core of attention?
3. What does the causal mask prevent, and why?
4. What are the two main sub-parts of a Transformer block, and the "talk vs think" intuition?

Next: [`02-training-llms.md`](02-training-llms.md) — how these models are actually trained at scale.
