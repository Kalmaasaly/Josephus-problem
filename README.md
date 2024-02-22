# Josephus Problem Solution

## Overview
This Python script provides a solution to the Josephus Problem, determining Joseph's survival position in a cave based on the number of soldiers present. The algorithm calculates the highest power of 2 less than or equal to the given number of soldiers and computes Joseph's survival site accordingly.

## Dependencies
- Python 3.x
- math module (standard library)

## Usage
1. Run the script by executing `python josephus_problem_solution.py` in the terminal.
2. Enter the number of soldiers in Joseph's Cave when prompted.
3. The script will calculate and display Joseph's survival position within the cave.

## Functions

### `highest_power_of_2(n: int) -> int`
Returns the highest power of 2 less than or equal to the given number 'n'.

#### Parameters
- `n` (int): The input integer for which the highest power of 2 needs to be calculated.

#### Returns
- int: The highest power of 2 less than or equal to 'n'.

### `get_number_soldiers(prompt: str) -> int`
Takes user input for the number of soldiers in Joseph's Cave, ensuring it's a non-negative integer.

#### Parameters
- `prompt` (str): The prompt to be displayed to the user.

#### Returns
- int: The number of soldiers entered by the user.

### `main() -> None`
The main function that calculates Joseph's survival position based on the number of soldiers in the cave.

## Example
```bash
How many soldiers are in Joseph's Cave? 20
Joseph's survival relies on being situated at 17
