# fifteen-puzzle-solver
Fifteen puzzle solver using graph traversal algorithms written in Python

Program allows to choose desired graph traversal algorithm from given below:
* astr - A* strategy, with distance algorithms:
	+ hamm - Hamming distance
	+ manh - Manhattan distance
* BFS - Breadth First Search strategy and
* DFS - Depth First Search strategy, with search order:
	+ DRLU
	+ DRUL
	+ LUDR
	+ LURD
	+ RDLU
	+ RDUL
	+ ULDR
	+ ULRD,
where D = down, U = UP, R = RIGHT, L = LEFT.

main.py CLI arguments:
* strategy: ”bfs”, ”dfs” or ”astr”
* strategyParam: heuristics ”hamm” or ”manh” in case of "astr" strategy, otherwise permutation search order, for example ”LRUD”
* initialStateFilePath: initial puzzle state file path (input)
* solutionFilePath: solution file path (output)
* statsFilePath: stats file path (output)

Initial state input file format:
```
puzzle_height puzzle_width
x x x x
x x x x
x x x x
x x x x
```

Solution output file format:
```
path_length solution_path(list of moves)
```

Stats output file format:
```
path_length
number_of_nodes_visited
number_of_nodes_fully_explored
maximum_recursion_depth
execution_time
```