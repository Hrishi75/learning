# 00 — Tokenization: how text becomes numbers

A neural network can only do math on numbers. But text is letters and words. So
the very first thing any LLM does is turn your text into numbers. That process is
**tokenization**, and understanding it explains a surprising number of LLM quirks
(why they're bad at spelling, why they miscount letters, why some languages cost
more).

---

## The core problem

You type: `"I love AI"`. The model can't multiply the word "love." It needs
numbers. So we need a dictionary that maps pieces of text to numbers.

The naive idea: give every **word** a number.
- `"I" -> 1`, `"love" -> 2`, `"AI" -> 3`

Problem: there are millions of words, plus typos, plus new words ("rizz",
"unfollowable"), plus other languages. A word dictionary would be gigantic and
still miss things.

The opposite naive idea: give every **letter** a number.
- `"l" -> 12`, `"o" -> 15`, ...

Problem: sequences get super long, and single letters carry almost no meaning, so
the model has to work harder.

**The compromise that won: subword tokens.** Break text into common *chunks* —
sometimes whole words, sometimes word-pieces. This is done by an algorithm called
**Byte Pair Encoding (BPE)**.

---

## How Byte Pair Encoding (BPE) works (the intuition)

BPE looks at a giant pile of text and greedily merges the most common adjacent
pairs of characters into single tokens. Repeat thousands of times.

Tiny illustration. Start with characters:

```
"l o w   l o w e r   l o w e s t"
```

The pair `l o` appears a lot -> merge it into `lo`. Then `lo w` is common ->
merge into `low`. After many merges, common words like `low` become a *single*
token, while rare words stay split into pieces. Final vocabulary might contain:
`low`, `er`, `est`, plus thousands of others.

Result: common words = 1 token, rare words = a few tokens, gibberish = many
tokens. Efficient and flexible — it can represent *any* text, even words it never
saw, by falling back to smaller pieces.

---

## See it yourself (real example)

A typical sentence and how a real tokenizer might split it (each `|` is a token
boundary):

```
"Tokenization is fascinating!"
   ->  | Token | ization |  is |  fascinating | ! |
```

Notice:
- "Token" and "ization" split apart (one is common, one less so).
- The space before a word is usually glued to it (` is`, ` fascinating`).
- Punctuation is often its own token.

Try it in code (uses OpenAI's `tiktoken`, but any tokenizer shows the idea):

```python
# pip install tiktoken
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

text = "I love AI security!"
ids = enc.encode(text)
print("token ids:", ids)
print("num tokens:", len(ids))
for i in ids:
    print(repr(enc.decode([i])))   # show each token as text
```

You'll see the text become a list of integers (the token IDs), and you can decode
each ID back to its text chunk.

> Online, the **OpenAI Tokenizer** and **tiktokenizer.vercel.app** let you paste
> text and watch it split live. Highly recommended — play for 10 minutes.

---

## From token IDs to "embeddings" (the bridge to meaning)

A token ID like `15496` is just a label — it has no meaning by itself. The model
converts each ID into a vector of numbers called an **embedding**.

```
token "king"  -> id 7234 -> [0.21, -0.04, 0.88, ... ]   (e.g. 768 numbers)
```

This embedding vector is **learned during training**. The magic: the model
arranges these vectors so that *related meanings sit near each other* in this
high-dimensional space. The famous example:

```
vector("king") - vector("man") + vector("woman")  ≈  vector("queen")
```

Meaning is captured as *geometry*. Words about royalty cluster together; words
about food cluster elsewhere. The model never sees letters as meaningful — it
sees positions in this "meaning space." This is why embeddings are sometimes
called the model's "mental map" of concepts.

So the full pipeline so far:

```
text -> tokens (chunks) -> token IDs (integers) -> embeddings (vectors) -> [into the Transformer]
```

---

## Why tokenization explains weird LLM behavior (fun + important)

Knowing tokenization, you can now explain things that confuse most users:

1. **"Why can't it spell / reverse a word reliably?"**
   It doesn't see letters — it sees chunks. "strawberry" might be 2-3 tokens, so
   counting the r's means reasoning about something it can't directly see.

2. **"Why does it sometimes miscount letters?"** Same reason. Letters are hidden
   inside tokens.

3. **"Why do some languages cost more (more tokens = more money)?"**
   Tokenizers are trained mostly on English. English words are often 1 token;
   the same meaning in, say, Hindi or Thai may take many more tokens, so it's
   slower and pricier. This is a real *fairness* issue in AI.

4. **Context windows are measured in tokens, not words.** "8k context" means 8000
   tokens, roughly 6000 English words.

---

## Connection to AI security

Tokenization is an **attack surface**. Because the model thinks in tokens, not
characters, attackers can:
- Hide forbidden words by splitting them with odd spacing/unicode so they
  tokenize differently and slip past simple filters.
- Use rare-token or special-character tricks to confuse safety classifiers.
- Exploit the fact that a safety filter and the model may tokenize the same text
  differently.

We'll revisit this in folder 04 (jailbreaks). For now, just register: *the gap
between how humans read text and how models tokenize it is something attackers
abuse.*

---

## Check yourself

1. Why not just give every word its own number? Why not every letter?
2. What is an embedding, and what does "meaning is geometry" mean?
3. Give one real LLM quirk that tokenization explains.

Next: [`01-transformers-and-attention.md`](01-transformers-and-attention.md) —
the engine that processes these embeddings.
