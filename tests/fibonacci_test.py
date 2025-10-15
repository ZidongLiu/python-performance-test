"""
Fibonacci sequence benchmark test.
"""

from typing import Tuple
from .base_test import BaseBenchmarkTest, time_function


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


class FibonacciTest(BaseBenchmarkTest):
    """Benchmark test for Fibonacci sequence calculation."""
    
    def __init__(self, n: int = 25, repeats: int = 1):
        """
        Initialize Fibonacci test.
        
        Args:
            n: Fibonacci number to calculate (default: 25)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Fibonacci Sequence (n={n})", repeats)
        self.n = n
    
    def run_test(self) -> Tuple[int, float]:
        """
        Run Fibonacci benchmark.
        
        Returns:
            Tuple containing (fibonacci_result, execution_time)
        """
        return time_function(fibonacci, self.n)
