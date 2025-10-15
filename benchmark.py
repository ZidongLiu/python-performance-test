#!/usr/bin/env python3
"""
Example script that demonstrates running the same code across different Python versions.
This script can be executed with any of the three Python versions to show performance differences.
"""

import sys
import platform
import argparse

# Import benchmark tests from the tests package
from tests import (
    FibonacciTest,
    BubbleSortTest,
    ListComprehensionTest,
    FunctionCallTest,
    ExceptionHandlingTest,
    ObjectInstantiationTest,
    AttributeAccessTest
)


def run_benchmarks(repeats: int = 1) -> None:
    """
    Run all benchmarks and display results.
    
    Args:
        repeats: Number of times to repeat each test (default: 1)
    """
    print("=" * 60)
    print("Python Performance Test Results")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    if repeats > 1:
        print(f"Repeats per test: {repeats}")
    print("=" * 60)
    
    # Test 1: Fibonacci
    fibonacci_test = FibonacciTest(35, repeats)
    fibonacci_test.print_results()
    
    # Test 2: Bubble Sort
    bubble_sort_test = BubbleSortTest(5000, repeats)
    bubble_sort_test.print_results()
    
    # Test 3: List Comprehension
    list_comp_test = ListComprehensionTest(10000000, repeats)
    list_comp_test.print_results()
    
    # Test 4: Function Call Overhead
    function_call_test = FunctionCallTest(10000000, repeats)
    function_call_test.print_results()
    
    # Test 5: Exception Handling
    exception_test = ExceptionHandlingTest(10000000, repeats)
    exception_test.print_results()
    
    # Test 6: Object Instantiation
    object_inst_test = ObjectInstantiationTest(1000000, repeats)
    object_inst_test.print_results()
    
    # Test 7: Attribute Access
    attr_access_test = AttributeAccessTest(object_inst_test.results['result'], repeats)
    attr_access_test.print_results()
    
    print("\n" + "=" * 60)
    print("Benchmark completed!")
    print("=" * 60)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Run Python performance benchmarks")
    # parser.add_argument(
    #     "--repeats", 
    #     type=int, 
    #     default=1, 
    #     help="Number of times to repeat each test (default: 1)"
    # )
    # args = parser.parse_args()
    
    run_benchmarks(5)
