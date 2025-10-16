#!/usr/bin/env python3
"""
Example script that demonstrates running the same code across different Python versions.
This script can be executed with any of the three Python versions to show performance differences.
"""

import sys
import platform
import argparse

# Import benchmark functions from the tests package
from tests import (
    run_fibonacci_benchmark,
    run_bubble_sort_benchmark,
    print_bubble_sort_results,
    run_list_comprehension_benchmark,
    print_list_comprehension_results,
    run_function_call_benchmark,
    run_exception_handling_benchmark,
    run_object_instantiation_benchmark,
    run_attribute_access_benchmark,
    print_object_instantiation_results,
    print_benchmark_results
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
    fibonacci_results = run_fibonacci_benchmark(35, repeats)
    print_benchmark_results(fibonacci_results)
    
    # Test 2: Bubble Sort
    bubble_sort_results = run_bubble_sort_benchmark(5000, repeats)
    print_bubble_sort_results(bubble_sort_results)
    
    # Test 3: List Comprehension
    list_comp_results = run_list_comprehension_benchmark(10000000, repeats)
    print_list_comprehension_results(list_comp_results)
    
    # Test 4: Function Call Overhead
    function_call_results = run_function_call_benchmark(10000000, repeats)
    print_benchmark_results(function_call_results)
    
    # Test 5: Exception Handling
    exception_results = run_exception_handling_benchmark(10000000, repeats)
    print_benchmark_results(exception_results)
    
    # Test 6: Object Instantiation
    object_inst_results = run_object_instantiation_benchmark(1000000, repeats)
    print_object_instantiation_results(object_inst_results)
    
    # Test 7: Attribute Access
    attr_access_results = run_attribute_access_benchmark(object_inst_results['result'], repeats)
    print_benchmark_results(attr_access_results)
    
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
