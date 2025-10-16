"""
Performance test modules for Python version comparison.
This package contains individual benchmark tests that can be run across
different Python versions (3.13, 3.14, 3.14-threadfree).
"""

from .base_test import run_benchmark, print_benchmark_results, time_function
from .fibonacci_test import run_fibonacci_benchmark
from .sorting_test import run_bubble_sort_benchmark, print_bubble_sort_results
from .list_comprehension_test import run_list_comprehension_benchmark, print_list_comprehension_results
from .function_call_test import run_function_call_benchmark
from .exception_test import run_exception_handling_benchmark
from .object_test import run_object_instantiation_benchmark, run_attribute_access_benchmark, print_object_instantiation_results

__all__ = [
    'run_benchmark',
    'print_benchmark_results', 
    'time_function',
    'run_fibonacci_benchmark',
    'run_bubble_sort_benchmark',
    'print_bubble_sort_results',
    'run_list_comprehension_benchmark',
    'print_list_comprehension_results',
    'run_function_call_benchmark',
    'run_exception_handling_benchmark',
    'run_object_instantiation_benchmark',
    'run_attribute_access_benchmark',
    'print_object_instantiation_results'
]
