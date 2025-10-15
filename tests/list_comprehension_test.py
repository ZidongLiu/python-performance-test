"""
List comprehension benchmark test.
"""

from typing import List, Tuple
from .base_test import BaseBenchmarkTest, time_function


def list_comprehension_test(size: int) -> List[int]:
    """
    Test list comprehension performance.
    
    Args:
        size: Size of the list to create
        
    Returns:
        List of squared integers
    """
    return [i * i for i in range(size)]


class ListComprehensionTest(BaseBenchmarkTest):
    """Benchmark test for list comprehension."""
    
    def __init__(self, size: int = 100000, repeats: int = 1):
        """
        Initialize list comprehension test.
        
        Args:
            size: Size of list to create (default: 100000)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"List Comprehension ({size:,} elements)", repeats)
        self.size = size
    
    def run_test(self) -> Tuple[List[int], float]:
        """
        Run list comprehension benchmark.
        
        Returns:
            Tuple containing (comprehension_result, execution_time)
        """
        return time_function(list_comprehension_test, self.size)
    
    def print_results(self) -> None:
        """Print formatted test results with list length."""
        if not self.results:
            self.execute()
        
        result_list = self.results['result']
        print(f"\n{self.results['name']}")
        print(f"   Length: {len(result_list)}")
        
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
