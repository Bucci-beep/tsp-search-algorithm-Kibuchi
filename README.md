# Travelling Salesman Problem (TSP) — AI for Search & Optimisation

This project implements and evaluates metaheuristic search algorithms for solving the **Travelling Salesman Problem (TSP)** as part of the *AI for Search & Optimisation* module.

The focus is on **search behaviour, neighbourhood design, and evaluation**, rather than machine learning.  
All experiments are implemented in Python and documented in a single Jupyter Notebook.

---

## Problem Overview

The Travelling Salesman Problem (TSP) is a classic combinatorial optimisation problem where the objective is to find the shortest possible tour that visits each city exactly once and returns to the starting city.

In this project:
- Cities are represented by Euclidean coordinates
- A tour is a permutation of city indices
- The objective function is the total tour length computed from a distance matrix
- A 50-city instance is used as the main benchmark, with smaller subsets for testing

---

## Algorithms Implemented

### 1. Tabu Search (Single-Solution Metaheuristic)

Tabu Search is implemented as the primary single-solution search algorithm, using:
- Move-based short-term memory (tabu list)
- Aspiration criterion
- Adaptive tabu tenure

Two neighbourhood structures are evaluated:

#### • Swap Neighbourhood (Baseline)
- Exchanges two cities in the tour
- Computationally inexpensive
- Converges quickly but often stagnates in local minima

#### • 2-opt Neighbourhood (Enhanced)
- Reverses segments of the tour
- Produces larger structural changes
- Enables deeper exploration of the search space
- Achieves lower final tour costs at a modest runtime cost

This within-algorithm comparison highlights the importance of neighbourhood design in local search.

---

### 2. Genetic Algorithm (Population-Based Metaheuristic)

The Genetic Algorithm (GA) provides a population-based comparison using:
- Permutation-based encoding
- Tournament selection
- PMX (Partially Mapped Crossover)
- Swap mutation
- Elitism

The GA explores multiple regions of the solution space in parallel and is evaluated against Tabu Search in terms of convergence, solution quality, and robustness.

---

## Evaluation & Experiments

The notebook includes:
- Convergence plots for all algorithms
- Final tour cost comparisons
- Runtime measurements
- A 20-run paired t-test to assess statistical significance

Key experimental comparisons:
- Tabu Search (swap) vs Tabu Search (2-opt)
- Tabu Search vs Genetic Algorithm
- Exploration vs exploitation trade-offs
- Solution quality vs computational cost

---

## Repository Structure
tsp-search-algorithm-Kibuchi/
│
├── tsp-search-algorithm-Kibuchi.ipynb # Main notebook (implementation + results)
├── README.md # Project overview
├── requirements.txt # Python dependencies
│
├── data/ # City coordinate data
├── algorithms/ # Algorithm-related helper code (if applicable)
├── src/ # Supporting utilities
└── docs/ # Report and supporting documents

## Report

The final project report is available in the `docs/` directory.
The report PDF includes the project title, author name, and student ID, as required for submission.

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/tsp-search-algorithm-Kibuchi.git
cd tsp-search-algorithm-Kibuchi

2. Install dependencies:
pip install -r requirements.txt

3. Open notebook:
jupyter notebook tsp-search-algorithm-Kibuchi.ipynb

4. Run cells top to bottom to reproduce all results and figures.

Key Takeaways

Neighbourhood choice has a significant impact on Tabu Search performance

2-opt enables Tabu Search to escape deeper local minima than simple swaps

Population-based methods (GA) provide stronger global exploration

Statistical evaluation is essential when algorithms involve randomness

Practical runtime behaviour can differ from theoretical expectations

Module Context

This project was developed for the AI for Search & Optimisation module assignment and focuses on:

Heuristic and metaheuristic search

Algorithm design decisions

Empirical evaluation and analysis

Author

Denis Kibuchi
MSc Artificial Intelligence
University of the West of England (UWE Bristol)