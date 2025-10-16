"""
List comprehension benchmark test.
"""

from typing import List
from .base_test import run_benchmark


def list_comprehension_test(size: int) -> List[int]:
    """
    Test list comprehension performance.
    
    Args:
        size: Size of the list to create
        
    Returns:
        List of squared integers
    """
    return [i * i for i in range(size)]


def run_list_comprehension_benchmark(size: int = 100000, repeats: int = 1) -> dict:
    """
    Run list comprehension benchmark.
    
    Args:
        size: Size of list to create (default: 100000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"List Comprehension ({size:,} elements)", 
                          list_comprehension_test, size, repeats=repeats)
    return results


def print_list_comprehension_results(results: dict) -> None:
    """Print formatted list comprehension test results with list length."""
    result_list = results['result']
    print(f"\n{results['name']}")
    print(f"   Length: {len(result_list)}")
    
    if results['repeats'] == 1:
        print(f"   Time: {results['execution_times'][0]:.6f} seconds")
    else:
        stats = results['statistics']
        print(f"   Repeats: {results['repeats']}")
        print(f"   Mean Time: {stats['mean']:.6f} seconds")
        print(f"   Min Time:  {stats['min']:.6f} seconds")
        print(f"   Max Time:  {stats['max']:.6f} seconds")
        print(f"   Std Dev:   {stats['std_dev']:.6f} seconds")
        print(f"   Median:    {stats['median']:.6f} seconds")
