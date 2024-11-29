
# Pacman AI Search Agent

This repository contains an implementation of search algorithms (DFS, BFS, UCS) in the context of the Pacman AI project. The goal is to control Pacman in a maze using different search strategies, including Depth-First Search (DFS), Breadth-First Search (BFS), and Uniform Cost Search (UCS).


The project was originally developed for educational purposes as part of UC Berkeley's CS 188 course on Artificial Intelligence. For more information on the project, visit the official [UC Berkeley AI Project Overview](https://ai.berkeley.edu/project_overview.html).

## Algorithms Implemented

- **Depth-First Search (DFS)**
- **Breadth-First Search (BFS)**
- **Uniform Cost Search (UCS)**

These search algorithms can be used to find the shortest path to a goal (or across multiple goals) in a maze, depending on the strategy used.


## Running the Game

We can run the Pacman game with the search agent by using the following commands. Each search algorithm (DFS, BFS, and UCS) can be selected via the -a fn= algorithm flag.

1. For Depth-First Search (DFS):
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
2. For Breadth-First Search (BFS):
    ```bash
    python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
3. For Uniform Cost Search (UCS):
   ```bash
   python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
Replace mediumMaze with other maze layouts like tinyMaze, bigMaze, etc. for testing with different complexities.

## Time Comparison of Search Algorithms

| Algorithm | Big Maze | Medium Maze | Small  Maze |
|   :---:   |     :---:      |          :---: |          :---: |
| BFS   | 0.008530 seconds     | 0.004862 seconds   | 0.002660 seconds |
| DFS   | 0.006280 seconds    | 0.004183 seconds  |0.001868 seconds|
| UCS  | 0.008428 seconds   | 0.005010 seconds |0.002869 seconds|

## ScreenShots:

![image](https://github.com/user-attachments/assets/8c83e7ef-bfb5-483a-a140-115955eb973b)


