[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wHmfzksI)
# HW01 — Cables and Devices (Build a Graph + Degrees)

**Story intro.**  
You manage a small office network. Each device is linked to others by a cable. You get a list of cable pairs. You need a data model to answer simple questions like “who is connected to whom?” and “how many cables touch each device?”

**Technical description.**  
- **Input:** A list of edges like `[('PC1','SW1'), ('SW1','PR1')]`. Edges are undirected (a cable links both ways).  
- **Output:**  
  - `build_graph(edges, directed=False)` → adjacency list `dict` mapping node → list of neighbors.  
  - `degree_dict(graph)` → `dict` node → number of neighbors (for `directed=True`, this is **out-degree**).  
- **Constraints:**  
  - Node names are hashable strings.  
  - No external libraries.  
  - Edge pairs may repeat; handle by adding neighbors each time (duplicates allowed for HW01; we will ignore multi-edges).  
- **Expected complexity:** `build_graph` runs in **O(E)** time, uses **O(V+E)** space. `degree_dict` runs in **O(V+E)**.

## ESL scaffold with the 8 Steps
**Steps 1–5 (explicit prompts)**
1. **Read & Understand:** What does an edge mean here? Is it one-way or two-way?  
2. **Re-phrase:** Say it in your words: “Make a dictionary of neighbors.”  
3. **Identify I/O:** What is the input shape? What is the output shape?  
4. **Break down:** How will you add keys for new nodes? How do you add both directions for undirected?  
5. **Pseudocode:** Write 5–7 lines to loop through edges and fill the dictionary.

**Steps 6–8 (hints)**
- **Write code:** Turn your pseudocode into Python loops and `dict` updates.  
- **Debug:** Print the dict for a tiny example. Check one node by hand.  
- **Optimize:** State big-O. Explain in one sentence.

## Hints (not spoilers)
- Start with an empty dict. Create empty lists when you first see a node.  
- For undirected, append twice: `u→v` and `v→u`.  
- Degrees are just `len(graph[node])`.

## Run tests locally
```bash
python -m pytest -q
```
## FAQ
Q: Python version? A: 3.10 or 3.11.

Q: Should I read from stdin? A: No. Write the functions. Tests import them.

Q: Big-O I should state? A: build_graph O(E) time, O(V+E) space; degree_dict O(V+E).

Q: Duplicated edges? A: You may keep duplicates; degrees will count them.

Q: Self-loop (u,u)? A: Allowed; degree increases by 1 in undirected (neighbor list gets one u).

Q: Why did pytest fail to import? A: Ensure your functions are in main.py and named as shown.

Q: How are points given? A: 70% tests, 30% README with Steps and complexity note.