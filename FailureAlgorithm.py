# Failure function for pattern matching algorithms (e.g. KMP)

def compute_failure(pattern: str) -> list:
    
    # Length of the pattern.
    n = len(pattern)
    # if the pattern is empty, return an empty list.
    if n == 0:     
        return []
    
    # Initialize the failure function array with zeros.
    f = [0] * n
    # t is the length of the current prefix- suffix match.
    t = 0

    # Iterate through the pattern starting from the second character (position 1).
    for s in range(1, n):

        # If character do not match, reduce t using previously computed failure values.
        while t > 0 and pattern[t] != pattern[s]:
            t = f[t - 1]

        # If characters match, extend the prefix-suffix length.
        if pattern[t] == pattern[s]:
            t += 1
            f[s] = t
        # if no match, failure value remains 0.
        else:
            f[s] = 0

    # return the computed failure function.
    return f

# Solving Exercise 3.4.3 (page 137)

# Prints the patterns, positions and their failure function.
def _print_failure(pattern: str, f: list) -> None:
    n = len(pattern)
    print(f"Pattern: {pattern}")
    print(f"Positions (1..{n}): {list(range(1, n+1))}")
    print(f"Failure f:       {f}")
    print()

# Main program execution.
if __name__ == '__main__':

    # List of example patterns to test the algorithm.
    examples = [
        'abababaab',
        'aaaaaa',
        'abbaabb',
    ]

    # Compute and print the failure function for each example pattern.
    for p in examples:
        f = compute_failure(p)
        _print_failure(p, f)