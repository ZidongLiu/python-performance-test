"""
Function call overhead benchmark test.
"""

from typing import Tuple
from .base_test import BaseBenchmarkTest, time_function


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


class FunctionCallTest(BaseBenchmarkTest):
    """Benchmark test for function call overhead."""
    
    def __init__(self, iterations: int = 100000, repeats: int = 1):
        """
        Initialize function call test.
        
        Args:
            iterations: Number of function calls (default: 100000)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Function Call Overhead ({iterations:,} calls)", repeats)
        self.iterations = iterations
    
    def run_test(self) -> Tuple[int, float]:
        """
        Run function call overhead benchmark.
        
        Returns:
            Tuple containing (sum_result, execution_time)
        """
        return time_function(function_call_overhead_test, self.iterations)
