# Glossary — Every Term, Plain English

Quick lookups. When you meet a new term while reading the folders or papers, find
it here. Add your own as you go. Organized roughly from basics → advanced.

---

## Foundations
- **AI (Artificial Intelligence):** machines doing tasks that seem to require intelligence.
- **ML (Machine Learning):** machines that learn rules from data instead of being
  hand-programmed.
- **Deep Learning:** ML using neural networks with many layers.
- **Neural network:** layers of simple units ("neurons") that transform numbers;
  learns by adjusting weights.
- **Weights / parameters:** the numbers a model learns. "70B" = 70 billion of them.
- **Bias (in a neuron):** a constant added to a neuron's weighted sum (NOT the
  fairness kind of bias).
- **Vector:** an ordered list of numbers. **Matrix:** a grid of numbers.
- **Dot product:** multiply two vectors element-wise and sum; measures similarity.
  The most-used operation in deep learning.
- **Activation function:** a non-linear "squish" (e.g. ReLU, sigmoid) that lets
  networks learn complex patterns.
- **Gradient:** the slope of the error w.r.t. each weight — "which way reduces error."
- **Gradient descent:** the training algorithm — step weights downhill along the gradient.
- **Backpropagation:** the chain-rule procedure that computes gradients through all layers.
- **Learning rate:** step size in gradient descent. Too big overshoots; too small is slow.
- **Loss / cost:** a number measuring how wrong the model is; training minimizes it.
- **Epoch:** one full pass over the training data.
- **Autograd:** automatic gradient computation (e.g. PyTorch's `loss.backward()`).

## Probability / output
- **Logits:** raw, unnormalized output scores before softmax.
- **Softmax:** turns logits into probabilities that sum to 1.
- **Temperature:** randomness knob on sampling. Low = focused/deterministic, high =
  creative/random.
- **Hallucination:** model confidently outputs false information.

## LLMs & Transformers
- **LLM (Large Language Model):** a big neural net trained to predict the next token.
- **Token:** a chunk of text (word or word-piece) the model processes as a unit.
- **Tokenization / BPE (Byte Pair Encoding):** splitting text into tokens by merging
  common character pairs.
- **Embedding:** a learned vector representing a token's meaning; related meanings
  sit near each other.
- **Transformer:** the neural architecture behind modern LLMs; built on attention.
- **Attention:** mechanism letting each token gather info from relevant other tokens.
- **Query / Key / Value (Q/K/V):** the three learned vectors per token that drive
  attention (query asks, key advertises, value is the info handed over).
- **Self-attention:** tokens in one sequence attending to each other.
- **Multi-head attention:** several attention operations in parallel, each learning a
  different relationship.
- **Feed-forward network (FFN/MLP):** the per-token "thinking" sub-layer in a
  Transformer block; stores much of the model's knowledge.
- **Residual connection / residual stream:** shortcut adding a block's input to its
  output; the "highway" where information flows through the network.
- **Layer normalization:** a stabilizer keeping activation numbers in a healthy range.
- **Causal / autoregressive mask:** prevents a token from attending to future tokens,
  so generation is left-to-right.
- **Context window:** how many tokens the model can attend to at once (its working memory).
- **In-context learning:** learning a task from examples given in the prompt, without
  weight updates.
- **Inference:** using a trained model to generate output (vs. training it).

## Training stages
- **Pretraining:** stage 1 — learn next-token prediction on huge text. Produces a **base model.**
- **Base / foundation model:** raw pretrained model; a text completer, not an assistant.
- **Fine-tuning:** further training a pretrained model on narrower data.
- **SFT (Supervised Fine-Tuning):** stage 2 — train on curated example conversations to
  make an assistant.
- **Instruct / chat model:** a model fine-tuned to follow instructions and converse.
- **Scaling laws:** performance improves predictably with more parameters, data, compute.
- **Chinchilla-optimal:** the compute-optimal balance of model size vs. training data.
- **Emergent abilities:** capabilities that appear (sometimes suddenly) only at larger scale.
- **Distillation:** training a smaller/cheaper model to imitate a bigger one's outputs.

## Alignment
- **Alignment:** making a model actually pursue intended goals, including as it scales.
- **Misalignment:** model pursues something other than what we intended.
- **HHH:** Helpful, Honest, Harmless — Anthropic's target properties.
- **Specification gaming:** optimizing the literal reward in unintended ways (genie problem).
- **Reward hacking:** exploiting flaws in the reward signal rather than doing the real task.
- **Goal misgeneralization:** learning a lookalike goal that diverges out of distribution.
- **Sycophancy:** telling users what they want to hear (an RLHF side effect).
- **Deceptive alignment:** appearing aligned while actually pursuing a different goal.
- **RLHF (RL from Human Feedback):** align a model using human preference comparisons +
  a reward model + RL (PPO).
- **Reward model (RM):** a model trained to predict human preference scores.
- **PPO (Proximal Policy Optimization):** the RL algorithm commonly used in RLHF.
- **KL penalty:** the "leash" keeping the RL-tuned model close to its original self.
- **DPO (Direct Preference Optimization):** align directly from preference pairs, no
  separate reward model or RL loop.
- **RLAIF (RL from AI Feedback):** RLHF but an AI gives the feedback.
- **Constitutional AI (CAI):** Anthropic method where the model critiques/revises itself
  against written principles ("a constitution").

## Security
- **Prompt injection:** sneaking instructions into a model's input to hijack it.
  **Direct** (user types it) vs **indirect** (hidden in external content the model reads).
- **Jailbreak:** input that makes a model bypass its own safety rules.
- **Many-shot jailbreaking:** filling a long context with fake compliant examples to
  steer the model.
- **GCG (Greedy Coordinate Gradient):** optimization-based attack that finds adversarial
  suffix strings; transfers across models.
- **Adversarial example:** a tiny crafted input change that flips a model's output.
- **FGSM / PGD:** methods to craft adversarial examples using gradients (one-step / iterated).
- **Data poisoning:** corrupting training data to change what a model learns.
- **Backdoor / trojan:** a hidden behavior triggered by a secret signal; model acts normal otherwise.
- **Sleeper agent:** a backdoored model whose hidden behavior survives safety training
  (Anthropic paper).
- **Model extraction / stealing:** copying a model's behavior or weights via queries.
- **Membership inference:** determining whether a record was in the training data.
- **Training data extraction:** prompting a model to regurgitate memorized training data.
- **Exfiltration:** secretly sending data out to an attacker (a common injection payload goal).
- **Least privilege / privilege separation:** limit an agent's powers so a compromise
  does limited damage. Top practical defense.
- **Instruction hierarchy:** training a model to trust system > developer > user > content.
- **Responsible disclosure:** privately reporting a vulnerability to the vendor before
  publicizing it.

## Red teaming, evals, oversight
- **Red teaming:** systematically attacking your own system to find failures before
  adversaries do.
- **Attack Success Rate (ASR):** fraction of attack attempts that succeed.
- **Over-refusal / false refusal:** wrongly refusing benign requests (cost of safety).
- **Eval (evaluation):** a structured test measuring a capability or safety property.
- **Dangerous capability evaluation:** testing for abilities that could cause serious
  harm (bio, cyber, autonomy, deception).
- **Capability elicitation:** trying hard (prompting, fine-tuning, tools) to surface a
  capability so absence claims are trustworthy.
- **Contamination:** test data leaking into training, inflating scores.
- **Goodhart's law:** "when a measure becomes a target, it stops being a good measure."
- **RSP (Responsible Scaling Policy):** Anthropic policy tying deployment to measured risk.
- **ASL (AI Safety Levels):** tiered risk levels (à la biosafety) requiring stronger
  safeguards as capabilities rise.
- **Scalable oversight:** supervising models at/above human capability.
- **AI Debate:** two AIs argue opposite sides before a judge to surface truth.
- **Weak-to-strong generalization:** can a weak supervisor train a stronger model that
  exceeds the teacher? (analogy for humans supervising superhuman AI).

## Interpretability
- **Interpretability:** understanding what's happening inside a model.
- **Mechanistic interpretability (mech interp):** reverse-engineering the actual
  algorithms in the weights.
- **Feature:** an internal concept the model represents (e.g. "French text," "deception").
- **Circuit:** the computation connecting features (a learned mini-algorithm).
- **Induction head:** an attention head that completes patterns by copying earlier
  occurrences; tied to in-context learning.
- **Superposition:** storing more features than neurons via overlapping combinations.
- **Polysemantic neuron:** a neuron that activates for several unrelated concepts.
- **Monosemantic:** representing exactly one clean concept.
- **Sparse Autoencoder (SAE):** a tool that disentangles superposition into many sparse,
  interpretable features.
- **Ablation:** zeroing/removing a component to test whether it causes a behavior.
- **Steering:** turning a feature up/down to change behavior predictably.
- **Probing:** training a small classifier on internal activations to detect what info
  they contain.

## Tools / ecosystem
- **PyTorch:** the dominant deep-learning framework.
- **HuggingFace:** hub for open models, datasets, and the `transformers`/`trl` libraries.
- **TransformerLens:** library for mechanistic interpretability on small models.
- **tiktoken:** OpenAI's tokenizer library (good for *seeing* tokenization).
- **Inspect / lm-evaluation-harness:** frameworks for building and running evals.
- **TRL:** HuggingFace library for RLHF/DPO fine-tuning.

---

*Add new terms here as you meet them. A term you can define in plain English is a
term you understand.*
