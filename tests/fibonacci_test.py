"""
Fibonacci sequence benchmark test.
"""

from .base_test import run_benchmark


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: The position in the Fibonacci sequence
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci_benchmark(n: int = 25, repeats: int = 1) -> dict:
    """
    Run Fibonacci sequence benchmark.
    
    Args:
        n: Fibonacci number to calculate (default: 25)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Fibonacci Sequence (n={n})", fibonacci, n, repeats=repeats)
    return results
