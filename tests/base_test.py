"""
Base benchmark test class and utilities for performance testing.
"""

import time
import statistics
from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Tuple


class BaseBenchmarkTest(ABC):
    """Base class for all benchmark tests."""
    
    def __init__(self, name: str, repeats: int = 1):
        """
        Initialize the benchmark test with a name and repeat count.
        
        Args:
            name: Name of the benchmark test
            repeats: Number of times to repeat the test (default: 1)
        """
        self.name = name
        self.repeats = repeats
        self.results: Dict[str, Any] = {}
        self.execution_times: List[float] = []
        self.test_results: List[Any] = []
    
    @abstractmethod
    def run_test(self) -> Tuple[Any, float]:
        """
        Run the benchmark test and return (result, execution_time).
        
        Returns:
            Tuple containing the test result and execution time in seconds.
        """
        pass
    
    def execute(self) -> Dict[str, Any]:
        """
        Execute the benchmark multiple times and store statistical results.
        
        Returns:
            Dictionary containing test results and statistical timing information.
        """
        self.execution_times = []
        self.test_results = []
        
        # Run the test multiple times
        for i in range(self.repeats):
            result, execution_time = self.run_test()
            self.test_results.append(result)
            self.execution_times.append(execution_time)
        
        # Calculate statistics
        stats = self._calculate_statistics()
        
        self.results = {
            'name': self.name,
            'repeats': self.repeats,
            'result': self.test_results[0] if self.test_results else None,  # First result
            'all_results': self.test_results,
            'execution_times': self.execution_times,
            'statistics': stats,
            'timestamp': time.time()
        }
        return self.results
    
    def _calculate_statistics(self) -> Dict[str, float]:
        """
        Calculate statistical measures for execution times.
        
        Returns:
            Dictionary containing statistical measures
        """
        if not self.execution_times:
            return {}
        
        if len(self.execution_times) == 1:
            return {
                'mean': self.execution_times[0],
                'min': self.execution_times[0],
                'max': self.execution_times[0],
                'std_dev': 0.0,
                'median': self.execution_times[0]
            }
        
        return {
            'mean': statistics.mean(self.execution_times),
            'min': min(self.execution_times),
            'max': max(self.execution_times),
            'std_dev': statistics.stdev(self.execution_times) if len(self.execution_times) > 1 else 0.0,
            'median': statistics.median(self.execution_times)
        }
    
    def print_results(self) -> None:
        """Print formatted test results with statistics."""
        if not self.results:
            self.execute()
        
        print(f"\n{self.results['name']}")
        print(f"   Result: {self.results['result']}")
        
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


def time_function(func: Callable, *args, **kwargs) -> Tuple[Any, float]:
    """
    Time the execution of a function.
    
    Args:
        func: Function to time
        *args: Positional arguments for the function
        **kwargs: Keyword arguments for the function
        
    Returns:
        Tuple containing (function_result, execution_time)
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return result, end_time - start_time

