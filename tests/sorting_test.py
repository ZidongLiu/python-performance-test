"""
Sorting algorithm benchmark tests.
"""

from typing import List, Tuple
from .base_test import BaseBenchmarkTest, time_function


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


class BubbleSortTest(BaseBenchmarkTest):
    """Benchmark test for bubble sort algorithm."""
    
    def __init__(self, size: int = 1000, repeats: int = 1):
        """
        Initialize bubble sort test.
        
        Args:
            size: Size of array to sort (default: 1000)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Bubble Sort ({size} elements)", repeats)
        self.size = size
        self.test_array = create_test_array(size, reverse=True)
    
    def run_test(self) -> Tuple[List[int], float]:
        """
        Run bubble sort benchmark.
        
        Returns:
            Tuple containing (sorted_array, execution_time)
        """
        return time_function(bubble_sort, self.test_array)
    
    def print_results(self) -> None:
        """Print formatted test results with first 5 elements."""
        if not self.results:
            self.execute()
        
        sorted_array = self.results['result']
        print(f"\n{self.results['name']}")
        print(f"   First 5 elements: {sorted_array[:5]}")
        
        if self.repeats == 1:
            print(f"   Time: {self.results['execution_times'][0]:.6f} seconds")
        else:
            stats = self.results['statistics']
            print(f"   Repeats: {self.repeats}")
            print(f"   Mean Time: {stats['mean']:.6f} seconds")
            print(f"   Min Time:  {stats['min']:.6f} seconds")
            print(f"   Max Time:  {stats['max']:.6f} seconds")
            print(f"   Std Dev:   {stats['std_dev']:.6f} seconds")
            print(f"   Median:    {stats['median']:.6f} seconds")
