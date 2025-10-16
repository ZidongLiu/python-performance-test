"""
Sorting algorithm benchmark tests.
"""

from typing import List
from .base_test import run_benchmark


def create_test_array(size: int, reverse: bool = True) -> List[int]:
    """
    Create a test array for sorting benchmarks.
    
    Args:
        size: Size of the array
        reverse: If True, create reverse sorted array
        
    Returns:
        list of integers
    """
    if reverse:
        return list(range(size, 0, -1))
    return list(range(size))


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sort a list using bubble sort algorithm.
    
    Args:
        arr: list of integers to sort
        
    Returns:
        Sorted list of integers
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify the original
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def run_bubble_sort_benchmark(size: int = 1000, repeats: int = 1) -> dict:
    """
    Run bubble sort benchmark.
    
    Args:
        size: Size of array to sort (default: 1000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    test_array = create_test_array(size, reverse=True)
    results = run_benchmark(f"Bubble Sort ({size} elements)", bubble_sort, test_array, repeats=repeats)
    return results


def print_bubble_sort_results(results: dict) -> None:
    """Print formatted bubble sort test results with first 5 elements."""
    sorted_array = results['result']
    print(f"\n{results['name']}")
    print(f"   First 5 elements: {sorted_array[:5]}")
    
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
