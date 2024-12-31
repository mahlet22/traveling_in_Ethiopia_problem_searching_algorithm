# Traveling Ethiopia Problem

## Overview
This project solves the **Traveling Ethiopia Problem**, where an AI agent navigates a road network between cities in Ethiopia. The tasks include:
1. Traversing all cities using BFS or DFS on a **normal static road network**.
2. Handling **dynamic road conditions** (e.g., blocked roads).
3. Computing the **k-shortest paths** between two cities.

The road network is represented as a graph using **NetworkX**, with cities as nodes and roads (with distances) as edges.

---

## How to Run the Project
### Prerequisites
1. Install Python 3.x.
2. Install the required libraries by running:
   ```bash
   pip install networkx matplotlib
# run command 
python main_normal.py
python main_dynamic.py
python main_k_shortest.py
