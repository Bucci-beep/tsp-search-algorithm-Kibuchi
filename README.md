TSP Search Algorithms — Hill Climbing & Tabu Search

This project implements and compares Hill Climbing and Tabu Search for solving a 50-city Travelling Salesman Problem (TSP).
It follows the AI for Search & Optimisation module at UWE Bristol and demonstrates:

Local search design

Neighbourhood generation

Objective function evaluation

Short-term memory (Tabu)

Visual comparison of search behaviour

     Project Structure
tsp-search-algorithm-Kibuchi/
│
├── tsp_search.ipynb          # Main Jupyter notebook
│
├── data/
│   └── cities.csv            # 50-city dataset
│
├── algorithms/
│   ├── hill_climbing.py
│   ├── tabu_search.py
│   ├── neighbourhood.py
│   └── tsp_core.py
│
├── utils/
│   └── utils.py
│
└── README.md

     How to Run the Notebook
1. Clone the repository
git clone https://github.com/<your-username>/tsp-search-algorithm-Kibuchi.git
cd tsp-search-algorithm-Kibuchi

2. Install requirements
pip install numpy pandas matplotlib

3. Run the notebook
jupyter notebook


Then open:

tsp_search.ipynb


Run all cells sequentially.

📈 Algorithms Implemented
Hill Climbing

Swap neighbourhood

Best-improvement strategy

Terminates at local optimum

Tabu Search

Tabu list matrix

Tabu tenure

Aspiration criterion

Best-improving move with tabu restrictions

📊 Visualisations

The notebook generates:

Hill Climbing cost curve

Tabu Search cost curve

Combined comparison plot

These support evaluation and analysis.