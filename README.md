<div align="center">

# 🧩 SAT Reduction Visualizer

### *Visual Exploration of NP-Completeness and Boolean Satisfiability*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![SAT](https://img.shields.io/badge/SAT-Solver-green?style=for-the-badge)](https://github.com/pysathq/pysat)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

![Complexity Theory](https://img.shields.io/badge/Complexity-NP--Complete-red?style=for-the-badge)
![Educational](https://img.shields.io/badge/Type-Educational-purple?style=for-the-badge)

**An interactive framework that demonstrates how diverse computational problems reduce to Boolean satisfiability (SAT)**

[🚀 Quick Start](#-quick-start) • [🎯 What This Shows](#-what-this-project-demonstrates) • [🧠 How It Works](#-the-sat-reduction-pipeline) • [📚 Theory](#-theoretical-foundation)

</div>

---

## 💡 **What is This Project?**

This is a **SAT Reduction Visualizer** — an educational tool that demonstrates one of the deepest ideas in theoretical computer science:

> **Many completely different problems can be transformed into the same logical structure: Boolean satisfiability (SAT).**

### **The Core Idea:**

```
N-Queens
Graph Coloring        ───→  SAT  ───→  Solution
Sudoku
Scheduling
...
```

Thousands of seemingly unrelated problems share the **same computational structure**.

---

## 🎯 **What This Project Demonstrates**

This visualizer shows the complete pipeline:

```
Real-World Problem
      ↓
Logical Variables
      ↓
Constraints
      ↓
CNF Formula
      ↓
SAT Solver
      ↓
Solution Decoded
      ↓
Visualization
```

### **Why This Matters:**

This demonstrates the **Cook-Levin Theorem** — the foundation of NP-completeness:

```
If SAT has a polynomial algorithm
         ↓
       then
         ↓
      P = NP
```

Your project is essentially a **laboratory for studying reductions** — the key to understanding P vs NP.

---

## 🧠 **The SAT Reduction Pipeline**

### **Step 1: Problem Definition**

Example: **N-Queens**
```
Place N queens on an N×N chessboard
so no two queens attack each other
```

---

### **Step 2: Variable Encoding**

Define Boolean variables:
```
x(i,j) = True  ⟺  Queen at row i, column j
```

For N=4:
```
x(1,1), x(1,2), x(1,3), x(1,4)
x(2,1), x(2,2), x(2,3), x(2,4)
x(3,1), x(3,2), x(3,3), x(3,4)
x(4,1), x(4,2), x(4,3), x(4,4)
```

---

### **Step 3: Constraint Formulation**

#### **Constraint 1: One queen per row**
```
(x(1,1) ∨ x(1,2) ∨ x(1,3) ∨ x(1,4))
```

#### **Constraint 2: No two queens in same column**
```
(¬x(1,1) ∨ ¬x(2,1))  — rows 1,2 column 1
(¬x(1,1) ∨ ¬x(3,1))  — rows 1,3 column 1
...
```

#### **Constraint 3: No diagonal attacks**
```
(¬x(1,1) ∨ ¬x(2,2))  — diagonal conflict
(¬x(1,2) ∨ ¬x(2,3))  — diagonal conflict
...
```

---

### **Step 4: CNF Formula**

All constraints combined:
```
(x₁ ∨ x₂ ∨ x₃ ∨ x₄)
∧ (¬x₁ ∨ ¬x₂)
∧ (¬x₁ ∨ ¬x₃)
∧ (¬x₂ ∨ ¬x₄)
∧ ...
```

This is **Conjunctive Normal Form (CNF)** — the input format for SAT solvers.

---

### **Step 5: SAT Solving**

The SAT solver (e.g., Glucose, MiniSat) searches for an assignment:
```
x₁ = True
x₂ = False
x₃ = True
...
```

That satisfies **all clauses**.

**Result:**
- ✅ **SAT** — Solution found
- ❌ **UNSAT** — No solution exists

---

### **Step 6: Decode Solution**

Map Boolean assignment back to the original problem:
```
x(1,2) = True  →  Queen at row 1, column 2
x(2,4) = True  →  Queen at row 2, column 4
x(3,1) = True  →  Queen at row 3, column 1
x(4,3) = True  →  Queen at row 4, column 3
```

---

### **Step 7: Visualization**

Display the solution graphically:
```
. Q . .
. . . Q
Q . . .
. . Q .
```

---

## 🎯 **Currently Supported Problems**

### 1️⃣ **N-Queens Problem**

**Variables:**
```
x(i,j) = Queen at position (i,j)
```

**Constraints:**
- ✅ One queen per row
- ✅ One queen per column
- ✅ No diagonal attacks

**CNF Encoding:**
```python
# One queen per row
for row in range(N):
    clause = [x(row,col) for col in range(N)]
    
# No two queens in same column
for col in range(N):
    for r1 in range(N):
        for r2 in range(r1+1, N):
            clause = [-x(r1,col), -x(r2,col)]
```

---

### 2️⃣ **Graph Coloring**

**Variables:**
```
x(v,c) = Vertex v has color c
```

**Constraints:**
- ✅ Each vertex has exactly one color
- ✅ Adjacent vertices have different colors

**CNF Encoding:**
```python
# Each vertex has one color
for vertex in V:
    clause = [x(vertex,c) for c in colors]
    
# No two colors for same vertex
for vertex in V:
    for c1, c2 in combinations(colors, 2):
        clause = [-x(vertex,c1), -x(vertex,c2)]
        
# Adjacent vertices different colors
for (u,v) in edges:
    for c in colors:
        clause = [-x(u,c), -x(v,c)]
```

---

## 🏗️ **System Architecture**

```
┌─────────────────────────────────────────┐
│         Problem Definition              │
│  (N-Queens, Graph Coloring, Sudoku)     │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│         Variable Generator              │
│  Creates Boolean variables x₁,x₂,...    │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│       Constraint Encoder                │
│  Converts rules → CNF clauses           │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│         CNF Formula Builder             │
│  (x₁ ∨ x₂) ∧ (¬x₁ ∨ x₃) ∧ ...         │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│         SAT Solver (Glucose)            │
│  Finds satisfying assignment            │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│         Solution Decoder                │
│  Maps Boolean values → problem solution │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│         Visualization Engine            │
│  Displays solution graphically          │
└─────────────────────────────────────────┘
```

---

## ⚡ **Quick Start**

### 📦 **Installation**

```bash
# Clone the repository
git clone https://github.com/sengobasar/sat-reduction-visualizer.git
cd sat-reduction-visualizer

# Install dependencies
pip install -r requirements.txt
```

**Dependencies:**
```
python-sat>=0.1.7    # SAT solver interface
networkx>=3.0        # Graph operations
matplotlib>=3.5.0    # Visualization
numpy>=1.24.0        # Numerical operations
```

---

### ▶️ **Usage**

#### **N-Queens Example:**

```python
from sat_visualizer import NQueensSolver

# Create solver
solver = NQueensSolver(n=8)

# Generate CNF
cnf = solver.encode()

# Solve
solution = solver.solve()

# Visualize
solver.visualize(solution)
```

**Output:**
```
✓ SAT
Solution found in 0.023s

. . . Q . . . .
. Q . . . . . .
. . . . . . Q .
. . Q . . . . .
. . . . . Q . .
. . . . . . . Q
Q . . . . . . .
. . . . Q . . .
```

---

#### **Graph Coloring Example:**

```python
from sat_visualizer import GraphColoringSolver
import networkx as nx

# Create graph
G = nx.Graph()
G.add_edges_from([(1,2), (2,3), (3,4), (4,1), (1,3)])

# Create solver
solver = GraphColoringSolver(graph=G, num_colors=3)

# Solve
solution = solver.solve()

# Visualize
solver.visualize(solution)
```

---

## 📐 **Theoretical Foundation**

### **The Cook-Levin Theorem**

This project demonstrates the core idea behind NP-completeness:

```
Problem P
    ↓
Reduction (polynomial time)
    ↓
   SAT
```

If we can reduce problem P to SAT in polynomial time, then:
- P is **at most as hard as SAT**
- SAT is **at least as hard as P**

### **Why SAT is NP-Complete**

1. **SAT is in NP** — solutions can be verified in polynomial time
2. **Every NP problem reduces to SAT** — Cook-Levin Theorem

Therefore:
```
If SAT ∈ P, then P = NP
```

### **CNF Formula Structure**

**Conjunctive Normal Form (CNF):**
```
Clause₁ ∧ Clause₂ ∧ Clause₃ ∧ ...
```

Where each clause is:
```
(literal₁ ∨ literal₂ ∨ literal₃ ∨ ...)
```

And each literal is:
```
xᵢ  or  ¬xᵢ
```

**Example:**
```
(x₁ ∨ ¬x₂ ∨ x₃) ∧ (¬x₁ ∨ x₂) ∧ (¬x₂ ∨ ¬x₃)
```

---

## 🔬 **Constraint Modeling Examples**

### **Example 1: At Least One (OR)**

**Rule:** "At least one of x₁, x₂, x₃ must be true"

**CNF:**
```
(x₁ ∨ x₂ ∨ x₃)
```

---

### **Example 2: At Most One**

**Rule:** "At most one of x₁, x₂, x₃ can be true"

**CNF:**
```
(¬x₁ ∨ ¬x₂)
(¬x₁ ∨ ¬x₃)
(¬x₂ ∨ ¬x₃)
```

---

### **Example 3: Exactly One**

**Rule:** "Exactly one of x₁, x₂, x₃ must be true"

**CNF:** Combine "at least one" + "at most one"
```
(x₁ ∨ x₂ ∨ x₃)
∧ (¬x₁ ∨ ¬x₂)
∧ (¬x₁ ∨ ¬x₃)
∧ (¬x₂ ∨ ¬x₃)
```

---

### **Example 4: Implication**

**Rule:** "If x₁ then x₂" (x₁ → x₂)

**CNF:**
```
(¬x₁ ∨ x₂)
```

Because: x₁ → x₂ ≡ ¬x₁ ∨ x₂

---

## 📊 **Complexity Analysis**

### **Variable Growth**

| Problem | N | Variables | Clauses |
|---------|---|-----------|---------|
| N-Queens | 4 | 16 | ~48 |
| N-Queens | 8 | 64 | ~280 |
| N-Queens | 16 | 256 | ~1,200 |

### **Observation:**

Variables grow as **O(N²)**  
Clauses grow as **O(N³)** or higher

This exponential growth is why SAT is **NP-complete**.

---

## 🚀 **Roadmap**

### ✅ **v1.0 — Current**

**Implemented:**
- ✅ N-Queens encoding & solving
- ✅ Graph Coloring encoding & solving
- ✅ CNF generation
- ✅ SAT solving via Glucose
- ✅ Solution visualization

---

### 🚧 **v2.0 — In Progress**

**Planned:**
- 🔄 Sudoku solver
- 🔄 Scheduling problems
- 🔄 3-SAT reduction
- 🔄 Circuit SAT

---

### 📋 **v3.0 — Future**

**Vision:**
- 🔮 SAT solver visualization (CDCL algorithm)
  - Decision steps
  - Unit propagation
  - Conflict analysis
  - Backtracking
  - Clause learning
- 🔮 Interactive constraint builder
- 🔮 Performance metrics dashboard
- 🔮 Complexity growth plots (N vs clauses)

---

## 📁 **Project Structure**

```
sat-reduction-visualizer/
│
├── encoders/
│   ├── nqueens.py          # N-Queens → SAT
│   ├── graph_coloring.py   # Graph Coloring → SAT
│   ├── sudoku.py           # Sudoku → SAT (planned)
│   └── base_encoder.py     # Abstract encoder class
│
├── solvers/
│   └── sat_solver.py       # SAT solver wrapper (Glucose)
│
├── visualizers/
│   ├── board_viz.py        # N-Queens board
│   ├── graph_viz.py        # Colored graphs
│   └── cnf_viz.py          # CNF formula display
│
├── utils/
│   ├── cnf_builder.py      # CNF formula construction
│   └── dimacs.py           # DIMACS format conversion
│
├── examples/
│   ├── nqueens_demo.py
│   └── graph_coloring_demo.py
│
├── requirements.txt
└── README.md
```

---

## 🎓 **Educational Value**

This project helps students understand:

### 1️⃣ **Reductions**
How to transform one problem into another

### 2️⃣ **NP-Completeness**
Why SAT is the "hardest" problem in NP

### 3️⃣ **Constraint Modeling**
The most valuable skill: translating real-world rules into Boolean logic

### 4️⃣ **Computational Complexity**
Why some problems are fundamentally hard

---

## 💡 **Key Insights**

### **The Power of SAT Modeling**

```
Different problems
        ↓
Same Boolean structure
        ↓
Same SAT solver
```

The solver doesn't know the original problem — it only sees clauses.

### **Most Important Skill**

**Not** the solver algorithm itself.

**But** learning how to translate:
```
Real-world rule  →  Boolean constraint
```

This is the **core insight** of computational problem-solving.

---

## 🔒 **Limitations**

**Honest assessment:**

1. **Exponential Growth** — Variables and clauses grow exponentially
2. **No Optimization** — Uses off-the-shelf solver (not custom)
3. **Limited Problems** — Currently only N-Queens and Graph Coloring (v1)
4. **No Solver Visualization** — Can't see internal SAT solver steps yet (v3)

---

## 🤝 **Contributing**

This is an educational research project. Contributions welcome!

**Priority areas:**
- 🧩 New problem encodings (Sudoku, TSP, Scheduling)
- 🔍 SAT solver visualization (CDCL algorithm)
- 📊 Performance analysis tools
- 📝 Educational documentation
- 🧪 Test cases

---

## 📚 **References**

**Books:**
- *The Art of Computer Programming* — Donald Knuth (SAT solving)
- *Computational Complexity* — Papadimitriou (NP-completeness)
- *Computers and Intractability* — Garey & Johnson (NP-complete problems)

**Papers:**
- Cook (1971) — "The Complexity of Theorem-Proving Procedures"
- Levin (1973) — "Universal Search Problems"
- Marques-Silva & Sakallah (1999) — "GRASP: A Search Algorithm for Propositional Satisfiability"

**Tools:**
- PySAT — Python SAT library
- Glucose SAT Solver
- MiniSat

---



<div align="center">

### ⭐ **If you find this project interesting, please star it!**

[![GitHub stars](https://img.shields.io/github/stars/sengobasar/sat-reduction-visualizer?style=social)](https://github.com/sengobasar/sat-reduction-visualizer)

**Made with 🧩 and 🧠**

---

**SAT Reduction Visualizer**

*Exploring the foundations of computational complexity through Boolean satisfiability*

</div>
