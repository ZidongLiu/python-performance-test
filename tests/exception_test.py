"""
Exception handling benchmark test.
"""

from .base_test import run_benchmark


def exception_handling_test(iterations: int) -> int:
    """
    Test exception handling performance.
    
    Args:
        iterations: Number of iterations to run
        
    Returns:
        Accumulated result from exception handling
    """
    result = 0
    for i in range(iterations):
        try:
            if i % 2 == 0:
                raise ValueError("Even number")
            result += i
        except ValueError:
            result += i * 2
        finally:
            result += 1
    
    return result


def run_exception_handling_benchmark(iterations: int = 10000, repeats: int = 1) -> dict:
    """
    Run exception handling benchmark.
    
    Args:
        iterations: Number of iterations (default: 10000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Exception Handling ({iterations:,} iterations)", 
                          exception_handling_test, iterations, repeats=repeats)
    return results
