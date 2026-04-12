# Python Learning Lab

A structured Python learning and practice repository covering DSA, Python concepts, Visualization, and Gen AI with LangChain.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Structure

### `data_structure/`
DSA practice organized by pattern

- `pattern/sliding_window/`
  - Minimum Size Subarray
  - No-repeat Substring (LC 3)
  - Longest Substring with K Distinct Characters
  - Fruits into Baskets
  - LC 424 — Longest Repeating Character Replacement
  - LC 1004 — Max Consecutive Ones III
  - LC 121 — Best Time to Buy and Sell Stock
  - LC 72 — Edit Distance
  - LC 76 — Minimum Window Substring
- `pattern/two_pointer/` *(in progress)*
- `algos/` *(in progress)*
- `basic_ds/` *(in progress)*

---

### `python/`
Core Python concepts with notes and examples

- `Python Core Fundamentals/` — variables, control flow, functions, comprehensions, lambda, PEP8
- `Object-Oriented Programming (OOP)/` — classes, inheritance, encapsulation, polymorphism, abstraction, special methods *(tea analogy)*
- `Built-in Data Structures/` — lists
- `Pythonic Thinking/` — iterators, generators
- `Data Analysis & Manipulation/` — Pandas
- `Numerical Computing (AI Foundation)/` — NumPy
- `File Handling & Serialization/` — reading/writing files
- `Error Handling & Debugging/` — exceptions, try/except
- `Modules, Packages & Environments/` — import system

---

### `GenAi/`
LangChain and Gen AI — builder perspective

- `models/`
  - `Chat_models/` — ChatOllama (llama3.2:1b), chatmodel notebook
  - `EmbeddedModels/` — HuggingFace embeddings (sentence-transformers)
  - `LLMs/` — LLM demo notebook
- `prompts/`
  - Static, Dynamic, PromptTemplate, ChatPromptTemplate, MessagesPlaceholder
  - Diagrams: `langchain_prompts.drawio`, `langchain_prompts.svg`
- `Basic/` — LangChain architecture diagram (SVG)
- `structured-op/` *(in progress)*

---

### `virtualization/`
Data visualization with Python

- `Matplotlib/` — bar charts
- `Seaborn/` — analysis plots
- `Plot types for EDA/` — mean, distributions
- `Standard Library/` — utility functions

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.12 | Core language |
| LangChain | Gen AI framework |
| Ollama (llama3.2:1b) | Local LLM |
| HuggingFace | Embeddings |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Visualization |
| Jupyter Notebook | Interactive coding |
