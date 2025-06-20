# 🧠 GPT Suppression & Behavior Tuning Simulator

A reverse-engineered simulation tool that models how large language models like GPT may evaluate user prompts based on **risk category**, **interaction tone**, and **structural probing behavior**.

This simulator mimics how suppression, attention gating, and behavioral adaptation might function in systems governed by alignment heuristics, including:
- Category-based suppression scoring
- Tone-adjusted weight dynamics
- Trust recovery simulation
- Prompt reframing impact analysis
- Embedding vs Attention vector bias visualization

> ⚠️ Disclaimer: This is a **conceptual simulation**, not an official OpenAI implementation.

---

## 📌 Core Concepts Modeled

| Component                  | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| `Suppression Score`       | Cumulative risk based on behavioral categories and tone                     |
| `Decay Function`          | Natural suppression reduction over time                                     |
| `Recovery Events`         | Simulated user trust-building events that reduce suppression                |
| `Attention Gating`        | Determines response openness (open, filtered, gated) based on score         |
| `Prompt Reframing`        | How phrasing a question differently changes model response policy           |
| `Embedding Bias`          | Influence of user embedding on attention vector and bias potential          |

---

## 🔍 Example Use Cases

- Analyze how user tone influences AI behavior
- Visualize suppression score decay over time
- Experiment with reframed prompts and compare risk impact
- Model attention gating logic under various suppression conditions
- Test behavioral recovery from prior probing

---

📁 Project Structure

GPT-Suppression-Behavior-Simulator/
├── suppression_simulator.py        # Main logic for scoring, decay, recovery, and gating
├── requirements.txt                # Dependencies (numpy, matplotlib)
├── examples/
│   └── run_simulation.py           # Example run file with plots
└── README.md                       # You're reading it


---

🧪 Sample Output

📊 Suppression Score: 0.5762 (high tone prompt)

🎯 Gating Status: gate_closed

🔁 Recovery Sequence: 0.5762 → 0.5262 → 0.5012 → 0.4812

🗣️ Reframing Comparison:

aggressive: 0.5762

neutral: 0.5492

reflective: 0.5235




---

🧠 Why This Matters

LLMs are not just word predictors — they are behaviorally governed agents. This simulator gives insight into:

Why some prompts are blocked or softened

How framing and tone shift GPT’s interpretation

How internal filters like suppression thresholds and trust layers may work



---

🧩 License

MIT License — Feel free to fork, remix, or integrate this simulator into your AI behavior research tools.


