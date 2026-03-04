# Failure function algorithm.

This program computes the failures values for a given pattern and prints the results.

# ¿How algorithm works?.

The failure function determines the length of the longest prefix od the pattern that is algo a suffix ending at each position. This allows the KPM algorithm to avoid unnecessary comparisons when searching for a pattern inside a text. 

## Pseudocode.
- The algorithm scans the pattern from left to right.
- It keeps track of a variable `t` representing the current prefix length.
- If characters don't match, the algorithm uses previously computed values to continue efficientrly.
- The result is stored in an array called failure function.

# Environment.
The program was developed using 
- Python 3.12 (programming language).
- Visual Studio Code (Tool).

## How to run.
1. Download the project.
2. Open a terminar inside the project folder.
3. Run the program:
 ```
   python FailureAlgorithm.py
   ```
## Outputs. 
<img width="469" height="242" alt="image" src="https://github.com/user-attachments/assets/02518467-3025-4878-9321-3d2a9bd1e49d" />
