
# AlphaBetaAgent Implementation for Pacman

This project implements an **Alpha-Beta Pruning** algorithm for the Pacman AI game. The `AlphaBetaAgent` enhances the Minimax algorithm by pruning branches in the game tree that do not influence the final decision, improving efficiency.

## How to Use

### Prerequisites
- Python 3.x
- The Pacman project files provided by UC Berkeley's AI course.

### Files
- `multiAgents.py`: Contains the `AlphaBetaAgent` class and other agents (e.g., MinimaxAgent, ReflexAgent).
- `pacman.py`: The main script to run the game.
- `util.py` and `game.py`: Utility files required for the game mechanics.

### Implementation
The `AlphaBetaAgent` class extends `MultiAgentSearchAgent` and overrides the `getAction` method to implement Alpha-Beta Pruning. Key features include:
- **Alpha and Beta Bounds**: These help prune irrelevant branches of the search tree.
- **Maximization and Minimization**: Pacman maximizes the score, while ghosts minimize it.
- **Anti-Stalling Mechanism**: Penalizes the "STOP" action to prevent Pacman from getting stuck.

### Running the Game
To test the `AlphaBetaAgent`, use the following command:

```bash
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
