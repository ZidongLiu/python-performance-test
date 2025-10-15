"""
Exception handling benchmark test.
"""

from typing import Tuple
from .base_test import BaseBenchmarkTest, time_function


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


class ExceptionHandlingTest(BaseBenchmarkTest):
    """Benchmark test for exception handling."""
    
    def __init__(self, iterations: int = 10000, repeats: int = 1):
        """
        Initialize exception handling test.
        
        Args:
            iterations: Number of iterations (default: 10000)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Exception Handling ({iterations:,} iterations)", repeats)
        self.iterations = iterations
    
    def run_test(self) -> Tuple[int, float]:
        """
        Run exception handling benchmark.
        
        Returns:
            Tuple containing (accumulated_result, execution_time)
        """
        return time_function(exception_handling_test, self.iterations)
