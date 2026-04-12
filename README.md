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
<summary><b>🪟 Sliding Window</b></summary>

<br/>

<!-- AUTO:sliding-window -->
| # | File |
|---|---|
| 1 | `Fruits into Baskets .py` |
| 2 | `LC 1004..py` |
| 3 | `LC121.py` |
| 4 | `LC3661.py` |
| 5 | `LC424.py` |
| 6 | `LC72.py` |
| 7 | `LC76.py` |
| 8 | `Longest Substring with K Distinct Character.py` |
| 9 | `No-repeat Substring.py` |
| 10 | `minimum_size_subarray.py` |

> **10 problems** · Pattern: Expand right → shrink left → O(n)
<!-- END:sliding-window -->

</details>

<details>
<summary><b>🐢🐇 Slow & Fast Pointer</b></summary>

<br/>

<!-- AUTO:slow-fast -->
| # | File |
|---|---|
| 1 | ` lc876.py` |
| 2 | `lc 141.py` |
| 3 | `lc 143.py` |
| 4 | `lc 202 .py` |
| 5 | `lc 234 .py` |
| 6 | `lc 287.py` |
| 7 | `lc142.py` |
| 8 | `lc457.py` |

> **8 problems** · Pattern: Two pointers at different speeds.
<!-- END:slow-fast -->

</details>

<details>
<summary><b>📈 Kadane's Algorithm</b></summary>

<br/>

<!-- AUTO:kadane -->
| # | File |
|---|---|
| 1 | `53. Maximum Subarray.py` |
| 2 | `LC 1186. Maximum Subarray Sum with One Deletion.py` |
| 3 | `LC 152. Maximum Product Subarray.py` |
| 4 | `Minmum SUbarray.py` |

> **4 problems** · Core: `current = max(arr[i], current + arr[i])`
<!-- END:kadane -->

</details>

<details>
<summary><b>➕ Prefix Sum</b></summary>

<br/>

<!-- AUTO:prefix-sum -->
| # | File |
|---|---|
| 1 | `974. Subarray Sums Divisible by K.PY` |
| 2 | `LC 525.py` |
| 3 | `pivot.py` |
| 4 | `subarray_sum_equal _k.py` |

> **4 problems** · Pattern: `prefix[i] = prefix[i-1] + arr[i]`
<!-- END:prefix-sum -->

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

<!-- AUTO:python-core -->
| Module | Files |
|---|---|
| **Python Core Fundamentals** | `comprehensions.py` · `control_flow.py` · `functions.py` · `input_output_comments_docstrings.py` · `lambda_functions.py` · `syntax_indentation_pep8.py` · `variable&simple_datatype.py` |
| **Object-Oriented Programming (OOP)** | `Classes and objects.py` · `abstraction.py` · `encapsulation.py` · `inheritance.py` · `polymorphism.py` · `special_methods.py` |
| **Built-in Data Structures** | `Dictionaries.py` · `Sets.py` · `Tuples.py` · `lists.py` |
| **Pythonic Thinking** | `Iterators and generators.py` |
| **File Handling & Serialization** | `Binary files & Pickle.py` · `CSV handling.py` · `JSON handling.py` · `Practice Questions.py` · `writing text files.py` |
| **Error Handling & Debugging** | `exceptions_try_except.py` |
| **Data Analysis & Manipulation** | `Pandas.py` |
| **Numerical Computing** | `NumPy.py` |
| **Modules & Environments** | `import system .py` |
<!-- END:python-core -->

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

<!-- AUTO:progress -->
| Module | Files | Status |
|---|---|---|
| Sliding Window | 10 | ✅ Complete (10 files) |
| Slow & Fast Pointer | 8 | ✅ Complete (8 files) |
| Kadane's Algorithm | 4 | ✅ Complete (4 files) |
| Prefix Sum | 3 | ✅ Complete (3 files) |
| Two Pointer | 0 | ⬜ Not Started |
| Algorithms | 0 | ⬜ Not Started |
| Python Core | 7 | ✅ Complete (7 files) |
| OOP | 6 | ✅ Complete (6 files) |
| Built-in DS | 4 | ✅ Complete (4 files) |
| File Handling | 5 | ✅ Complete (5 files) |
| Error Handling | 1 | ✅ Complete (1 files) |
| Data Analysis | 1 | ✅ Complete (1 files) |
| Numerical Computing | 1 | ✅ Complete (1 files) |
| Visualization | 4 | ✅ Complete (4 files) |
<!-- END:progress -->

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&pause=1000&color=6B7280&center=true&vCenter=true&width=500&lines=Built+with+curiosity.+Documented+with+intent." alt="footer" />

</div>
