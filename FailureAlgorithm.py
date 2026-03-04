def compute_failure(pattern: str) -> list:
    """Compute the KMP failure function for pattern.

    Returns a list f of length n where f[i] is the length of the
    longest proper prefix of pattern[:i+1] that is also a suffix.
    Indexing is 0-based for positions in the returned list.
    """
    n = len(pattern)
    if n == 0:     return []
    f = [0] * n
    t = 0
    for s in range(1, n):
        while t > 0 and pattern[t] != pattern[s]:
            t = f[t - 1]
        if pattern[t] == pattern[s]:
            t += 1
            f[s] = t
        else:
            f[s] = 0
    return f


def _print_failure(pattern: str, f: list) -> None:
    n = len(pattern)
    print(f"Pattern: {pattern}")
    print(f"Positions (1..{n}): {list(range(1, n+1))}")
    print(f"Failure f:       {f}")
    print()


if __name__ == '__main__':
    examples = [
        'abababaab',
        'aaaaaa',
        'abbaabb',
    ]
    for p in examples:
        f = compute_failure(p)
        _print_failure(p, f)