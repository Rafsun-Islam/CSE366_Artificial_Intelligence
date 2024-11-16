# Smartphone Inventory Management Simulation

This project simulates a **trading agent** for managing smartphone inventory, developed as part of **Lab Task 02**. The agent uses price and stock level percepts to make decisions about ordering more smartphones, adhering to specific rules and optimizing inventory management.

## Features

- **Percepts**:
  - **Price**: Current price of a specific smartphone model.
  - **Amount in Stock**: The quantity of smartphones available in the store.

- **Decision Rules**:
  1. If the price is **20% below the average price** and stock level is **not critically low (≥ 10 units)**, the agent orders **15 units**.
  2. If the stock level is **critically low (< 10 units)**, the agent orders **10 units**.
  3. Otherwise, the agent orders **0 units**.

- **Price Fluctuation**:
  - Gaussian distribution is used to simulate realistic price changes.
  - Mean: `0`, Standard Deviation: `50`.

- **Random Stock Consumption**:
  - Each time step, 1–3 units are randomly consumed.

- **Graphical Output**:
  - **Price Trends (Blue Line)**: Tracks the price of smartphones over time.
  - **Stock Levels (Green Line)**: Shows inventory levels at each time step.
  - **Units Bought (Orange Bars)**: Indicates the agent's purchasing behavior.

## Usage

### Prerequisites

- Python 3.x
- Required libraries:
  - `matplotlib`

### Running the Simulation

1. Copy the code into a Python file (e.g., `smartphone_agent.py`) or a Jupyter Notebook.
2. Run the script to execute the simulation.

### Output

- Logs detailing:
  - **Percepts**: Price and stock level at each time step.
  - **Actions Taken**: Number of units purchased.
  - **Updated Percepts**: State after applying the action.
- A graph visualizing price, stock levels, and purchasing decisions.

## Example Graph

The graph below represents a typical simulation run:


![image](https://github.com/user-attachments/assets/1c4fea4f-1674-455d-a652-a1bf70c6335e)


## License

This project is developed for educational purposes. Feel free to modify and reuse it for similar tasks.
