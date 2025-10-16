"""
Function call overhead benchmark test.
"""

from .base_test import run_benchmark


def function_call_overhead_test(iterations: int) -> int:
    """
    Test function call overhead.
    
    Args:
        iterations: Number of function calls to make
        
    Returns:
        Sum of all function call results
    """
    def simple_function(x: int) -> int:
        return x + 1
    
    result = 0
    for i in range(iterations):
        result += simple_function(i)
    
    return result


def run_function_call_benchmark(iterations: int = 100000, repeats: int = 1) -> dict:
    """
    Run function call overhead benchmark.
    
    Args:
        iterations: Number of function calls (default: 100000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Function Call Overhead ({iterations:,} calls)", 
                          function_call_overhead_test, iterations, repeats=repeats)
    return results
