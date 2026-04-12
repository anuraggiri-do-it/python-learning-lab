<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=32&pause=1000&color=3B82F6&center=true&vCenter=true&width=600&lines=Python+Learning+Lab+%F0%9F%90%8D;DSA+%7C+OOP+%7C+Gen+AI+%7C+Visualization;Built+from+first+principles." alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.4.3-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.1-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-llama3.2:1b-black?style=for-the-badge&logo=ollama&logoColor=white)

<br/>

> **A structured, hands-on Python learning repository** — built from first principles.  
> Covers DSA patterns, core Python, Gen AI with LangChain, and data visualization.  
> Every file is a focused, well-commented deep-dive — not just syntax, but *why* it works.

</div>

---

## ⚡ Quick Start

```bash
git clone https://github.com/anuraggiri-do-it/python-learning-lab.git
cd python-learning-lab
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🗂️ Repository Structure

```
python-learning-lab/
├── data_structure/          ← DSA patterns & algorithms
│   ├── pattern/
│   │   ├── sliding_window/
│   │   ├── slow and fast pointer/
│   │   ├── Kadane pattern/
│   │   ├── prefix _sum/
│   │   └── two_pointer/
│   ├── basic_ds/            ← Array, Linked List
│   └── algos/
├── python/                  ← Core Python concepts
│   ├── Python Core Fundamentals/
│   ├── Object-Oriented Programming (OOP)/
│   ├── Built-in Data Structures/
│   ├── Pythonic Thinking/
│   ├── Data Analysis & Manipulation/
│   ├── Numerical Computing (AI Foundation)/
│   ├── File Handling & Serialization/
│   ├── Error Handling & Debugging/
│   └── Modules, Packages & Environments/
├── GenAi/                   ← LangChain & Gen AI
│   ├── models/
│   ├── prompts/
│   └── Basic/
└── virtualization/          ← Data Visualization
    ├── Matplotlib/
    ├── Seaborn/
    ├── Plot types for EDA/
    └── Standard Library/
```

---

## 🧩 Data Structures & Algorithms

<details>
<summary><b>🪟 Sliding Window</b> — 10 problems</summary>

<br/>

| Problem | File | Complexity |
|---|---|---|
| Minimum Size Subarray Sum | `minimum_size_subarray.py` | O(n) / O(1) |
| No-repeat Substring (LC 3) | `No-repeat Substring.py` | O(n) / O(k) |
| Longest Substring K Distinct | `Longest Substring with K Distinct Character.py` | O(n) / O(k) |
| Fruits into Baskets | `Fruits into Baskets .py` | O(n) / O(1) |
| LC 424 — Longest Repeating Char Replacement | `LC424.py` | O(n) / O(1) |
| LC 1004 — Max Consecutive Ones III | `LC 1004..py` | O(n) / O(1) |
| LC 121 — Best Time to Buy and Sell Stock | `LC121.py` | O(n) / O(1) |
| LC 72 — Edit Distance | `LC72.py` | O(m×n) / O(m×n) |
| LC 76 — Minimum Window Substring | `LC76.py` | O(n) / O(k) |
| LC 3661 | `LC3661.py` | — |

> **Pattern:** Expand right → shrink left when condition is met. Each element is touched at most twice → O(n).

</details>

<details>
<summary><b>🐢🐇 Slow & Fast Pointer</b> — 8 problems</summary>

<br/>

| Problem | File |
|---|---|
| LC 141 — Linked List Cycle | `lc 141.py` |
| LC 142 — Linked List Cycle II | `lc142.py` |
| LC 143 — Reorder List | `lc 143.py` |
| LC 202 — Happy Number | `lc 202 .py` |
| LC 234 — Palindrome Linked List | `lc 234 .py` |
| LC 287 — Find the Duplicate Number | `lc 287.py` |
| LC 457 — Circular Array Loop | `lc457.py` |
| LC 876 — Middle of Linked List | `lc876.py` |

> **Pattern:** Two pointers at different speeds — fast catches slow when a cycle exists, or fast reaches end when it doesn't.

</details>

<details>
<summary><b>📈 Kadane's Algorithm</b> — 5 problems</summary>

<br/>

| Problem | File |
|---|---|
| LC 53 — Maximum Subarray | `53. Maximum Subarray.py` |
| LC 152 — Maximum Product Subarray | `LC 152. Maximum Product Subarray.py` |
| LC 1186 — Max Subarray Sum with One Deletion | `LC 1186. Maximum Subarray Sum with One Deletion.py` |
| Minimum Subarray | `Minmum SUbarray.py` |
| Pattern Deep-Dive Notes | `readme` |

> **Core decision:** `current = max(arr[i], current + arr[i])` — extend or restart?  
> **Mental model:** *"Greedy local optimism with a global memory."*

</details>

<details>
<summary><b>➕ Prefix Sum</b> — 4 problems</summary>

<br/>

| Problem | File |
|---|---|
| Subarray Sum Equals K | `subarray_sum_equal _k.py` |
| LC 525 — Contiguous Array | `LC 525.py` |
| 974 — Subarray Sums Divisible by K | `974. Subarray Sums Divisible by K.PY` |
| Pivot Index | `pivot.py` |

> **Pattern:** `prefix[i] = prefix[i-1] + arr[i]` — convert range-sum queries to O(1) lookups.

</details>

<details>
<summary><b>🔗 Basic Data Structures</b></summary>

<br/>

| Structure | File | Highlights |
|---|---|---|
| Array (`array` module) | `array.py` | Typed, contiguous memory, full CRUD + complexity notes |
| Linked List | `Linkedlist.py` | Node class, append/prepend/delete/search/reverse/display |

</details>

---

## 🐍 Python Core

<details>
<summary><b>Python Core Fundamentals</b></summary>

<br/>

| Topic | File |
|---|---|
| Variables & Data Types | `variable&simple_datatype.py` |
| Control Flow | `control_flow.py` |
| Functions — args, kwargs, recursion, type hints | `functions.py` |
| Comprehensions | `comprehensions.py` |
| Lambda Functions | `lambda_functions.py` |
| I/O, Comments, Docstrings | `input_output_comments_docstrings.py` |
| Syntax, Indentation, PEP8 | `syntax_indentation_pep8.py` |

</details>

<details>
<summary><b>Object-Oriented Programming (OOP)</b> — Tea Analogy 🍵</summary>

<br/>

> *Class = Recipe. Object = A cup of tea made from that recipe.*

| Concept | File |
|---|---|
| Classes & Objects | `Classes and objects.py` |
| Inheritance | `inheritance.py` |
| Encapsulation | `encapsulation.py` |
| Polymorphism | `polymorphism.py` |
| Abstraction | `abstraction.py` |
| Special / Dunder Methods | `special_methods.py` |

</details>

<details>
<summary><b>Built-in Data Structures</b></summary>

<br/>

`lists.py` · `Dictionaries.py` · `Sets.py` · `Tuples.py`

</details>

<details>
<summary><b>Pythonic Thinking</b></summary>

<br/>

`Iterators and generators.py`

</details>

<details>
<summary><b>File Handling & Serialization</b></summary>

<br/>

`Reading/writing text files.py` · `CSV handling.py` · `JSON handling.py` · `Binary files & Pickle.py` · `Practice Questions.py`

</details>

<details>
<summary><b>Error Handling & Debugging</b></summary>

<br/>

`exceptions_try_except.py` — try/except/else/finally, raising exceptions, custom exception classes.

</details>

<details>
<summary><b>Data Analysis & Numerical Computing</b></summary>

<br/>

`Pandas.py` · `NumPy.py` · `import system .py`

</details>

---

## 🤖 Gen AI with LangChain

```
GenAi/
├── models/
│   ├── Chat_models/     ← ChatOllama (llama3.2:1b)
│   ├── EmbeddedModels/  ← HuggingFace sentence-transformers
│   └── LLMs/            ← LLM demo notebook
├── prompts/
│   ├── Static & Dynamic prompts
│   ├── PromptTemplate & ChatPromptTemplate
│   ├── MessagesPlaceholder
│   ├── langchain_prompts.drawio
│   └── langchain_prompts.svg
├── Basic/               ← LangChain architecture diagram (SVG)
└── structured-op/       ← (in progress)
```

> Running a **local LLM** (llama3.2:1b via Ollama) + **HuggingFace embeddings** — no API keys needed.

---

## 📊 Visualization

```
virtualization/
├── Matplotlib/          ← bar.py
├── Seaborn/             ← anslysis.py
├── Plot types for EDA/  ← mean.py (distributions, mean plots)
└── Standard Library/    ← utils.py
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| Python | 3.12 | Core language |
| NumPy | 2.4.3 | Numerical computing |
| Pandas | 3.0.1 | Data manipulation |
| Matplotlib | latest | Visualization |
| Seaborn | latest | Statistical plots |
| scikit-learn | latest | ML utilities |
| LangChain | latest | Gen AI framework |
| Ollama (llama3.2:1b) | local | Local LLM inference |
| HuggingFace | sentence-transformers | Embeddings |
| python-dotenv | latest | Environment config |

---

## 📈 Progress

| Module | Status |
|---|---|
| Sliding Window | ✅ Complete |
| Slow & Fast Pointer | ✅ Complete |
| Kadane's Algorithm | ✅ Complete |
| Prefix Sum | ✅ Complete |
| Two Pointer | 🔄 In Progress |
| Algorithms | 🔄 In Progress |
| Python Core | ✅ Complete |
| OOP | ✅ Complete |
| Gen AI / LangChain | 🔄 In Progress |
| Visualization | ✅ Complete |

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&pause=1000&color=6B7280&center=true&vCenter=true&width=500&lines=Built+with+curiosity.+Documented+with+intent." alt="footer" />

</div>
