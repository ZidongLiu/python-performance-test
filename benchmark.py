#!/usr/bin/env python3
"""
Example script that demonstrates running the same code across different Python versions.
This script can be executed with any of the three Python versions to show performance differences.
Tests all 5 different data sizes for each test with 5 repetitions.
Results are saved to CSV format for analysis.
"""

import sys
import platform
import csv
from datetime import datetime
from pathlib import Path

# Import benchmark functions from the tests package
from tests import (
    run_fibonacci_benchmark,
    run_bubble_sort_benchmark,
    run_list_comprehension_benchmark,
    run_function_call_benchmark,
    run_exception_handling_benchmark,
    run_object_instantiation_benchmark,
    run_attribute_access_benchmark,
    run_multithread_cpu_benchmark,
    run_multithread_io_benchmark,
    run_concurrent_futures_cpu_benchmark,
    run_concurrent_futures_io_benchmark
)

# Test size arrays - 5 different sizes for each test type
FIBONACCI_SIZES = [20, 25, 30, 32, 35]
BUBBLE_SORT_SIZES = [1000, 2000, 3000, 4000, 5000]
LIST_COMPREHENSION_SIZES = [1000, 10000, 100000, 1000000, 10000000]
FUNCTION_CALL_SIZES = [1000, 10000, 100000, 1000000, 10000000]
EXCEPTION_SIZES = [1000, 10000, 100000, 1000000, 10000000]
OBJECT_COUNT_SIZES = [1000, 10000, 100000, 1000000, 5000000]
MULTITHREAD_CPU_SIZES = [2, 4, 8, 16, 32]  # Number of threads
MULTITHREAD_IO_SIZES = [2, 4, 8, 16, 32]  # Number of threads
MULTITHREAD_CPU_ITERATIONS = [50000, 100000, 200000, 500000, 1000000]  # Iterations per thread
MULTITHREAD_IO_DURATIONS = [0.005, 0.01, 0.02, 0.05, 0.1]  # Duration per task in seconds

# Size level names for display
SIZE_LEVELS = ["Small", "Medium", "Large", "XLarge", "XXLarge"]


def save_results_to_csv(results: list, filename: str) -> None:
    """
    Save benchmark results to CSV file.
    
    Args:
        results: List of result dictionaries
        filename: Output CSV filename
    """
    if not results:
        return
    
    # Create results directory if it doesn't exist
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    csv_path = results_dir / filename
    
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = [
            'test_name', 'test_type', 'size_level', 'size_value', 'python_version',
            'platform', 'architecture', 'repeats', 'mean_time', 'min_time', 'max_time',
            'std_dev', 'median_time', 'timestamp'
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            writer.writerow(result)
    
    print(f"Results saved to: {csv_path}")


def run_benchmarks(repeats: int = 5) -> None:
    """
    Run all benchmarks with 5 different data sizes and save results to CSV.
    
    Args:
        repeats: Number of times to repeat each test (default: 5)
    """
    print("=" * 60)
    print("Python Performance Test - Running Benchmarks")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Repeats per test: {repeats}")
    print("=" * 60)
    
    # Collect all results
    all_results = []
    timestamp = datetime.now().isoformat()
    
    # Test 1: Fibonacci - test all 5 sizes
    print("\nRunning Fibonacci tests...")
    for i, size in enumerate(FIBONACCI_SIZES):
        fibonacci_results = run_fibonacci_benchmark(size, repeats)
        stats = fibonacci_results['statistics']
        all_results.append({
            'test_name': fibonacci_results['name'],
            'test_type': 'Fibonacci',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 2: Bubble Sort - test all 5 sizes
    print("Running Bubble Sort tests...")
    for i, size in enumerate(BUBBLE_SORT_SIZES):
        bubble_sort_results = run_bubble_sort_benchmark(size, repeats)
        stats = bubble_sort_results['statistics']
        all_results.append({
            'test_name': bubble_sort_results['name'],
            'test_type': 'Bubble Sort',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 3: List Comprehension - test all 5 sizes
    print("Running List Comprehension tests...")
    for i, size in enumerate(LIST_COMPREHENSION_SIZES):
        list_comp_results = run_list_comprehension_benchmark(size, repeats)
        stats = list_comp_results['statistics']
        all_results.append({
            'test_name': list_comp_results['name'],
            'test_type': 'List Comprehension',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 4: Function Call Overhead - test all 5 sizes
    print("Running Function Call tests...")
    for i, size in enumerate(FUNCTION_CALL_SIZES):
        function_call_results = run_function_call_benchmark(size, repeats)
        stats = function_call_results['statistics']
        all_results.append({
            'test_name': function_call_results['name'],
            'test_type': 'Function Call',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 5: Exception Handling - test all 5 sizes
    print("Running Exception Handling tests...")
    for i, size in enumerate(EXCEPTION_SIZES):
        exception_results = run_exception_handling_benchmark(size, repeats)
        stats = exception_results['statistics']
        all_results.append({
            'test_name': exception_results['name'],
            'test_type': 'Exception Handling',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 6: Object Instantiation - test all 5 sizes
    print("Running Object Instantiation tests...")
    for i, size in enumerate(OBJECT_COUNT_SIZES):
        object_inst_results = run_object_instantiation_benchmark(size, repeats)
        stats = object_inst_results['statistics']
        all_results.append({
            'test_name': object_inst_results['name'],
            'test_type': 'Object Instantiation',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 7: Attribute Access - test all 5 sizes
    print("Running Attribute Access tests...")
    for i, size in enumerate(OBJECT_COUNT_SIZES):
        # Create objects for this size
        object_inst_results = run_object_instantiation_benchmark(size, repeats)
        # Test attribute access on these objects
        attr_access_results = run_attribute_access_benchmark(object_inst_results['result'], repeats)
        stats = attr_access_results['statistics']
        all_results.append({
            'test_name': attr_access_results['name'],
            'test_type': 'Attribute Access',
            'size_level': SIZE_LEVELS[i],
            'size_value': size,
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 8: Multi-thread CPU - test all 5 thread counts
    print("Running Multi-thread CPU tests...")
    for i, thread_count in enumerate(MULTITHREAD_CPU_SIZES):
        iterations = MULTITHREAD_CPU_ITERATIONS[i]
        multithread_cpu_results = run_multithread_cpu_benchmark(thread_count, iterations, repeats)
        stats = multithread_cpu_results['statistics']
        all_results.append({
            'test_name': multithread_cpu_results['name'],
            'test_type': 'Multi-thread CPU',
            'size_level': SIZE_LEVELS[i],
            'size_value': f"{thread_count} threads, {iterations:,} iter/thread",
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 9: Multi-thread I/O - test all 5 thread counts
    print("Running Multi-thread I/O tests...")
    for i, thread_count in enumerate(MULTITHREAD_IO_SIZES):
        duration = MULTITHREAD_IO_DURATIONS[i]
        multithread_io_results = run_multithread_io_benchmark(thread_count, duration, repeats)
        stats = multithread_io_results['statistics']
        all_results.append({
            'test_name': multithread_io_results['name'],
            'test_type': 'Multi-thread I/O',
            'size_level': SIZE_LEVELS[i],
            'size_value': f"{thread_count} threads, {duration}s/task",
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 10: Concurrent Futures CPU - test all 5 thread counts
    print("Running Concurrent Futures CPU tests...")
    for i, thread_count in enumerate(MULTITHREAD_CPU_SIZES):
        iterations = MULTITHREAD_CPU_ITERATIONS[i]
        concurrent_cpu_results = run_concurrent_futures_cpu_benchmark(thread_count, iterations, repeats)
        stats = concurrent_cpu_results['statistics']
        all_results.append({
            'test_name': concurrent_cpu_results['name'],
            'test_type': 'Concurrent Futures CPU',
            'size_level': SIZE_LEVELS[i],
            'size_value': f"{thread_count} threads, {iterations:,} iter/thread",
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Test 11: Concurrent Futures I/O - test all 5 thread counts
    print("Running Concurrent Futures I/O tests...")
    for i, thread_count in enumerate(MULTITHREAD_IO_SIZES):
        duration = MULTITHREAD_IO_DURATIONS[i]
        concurrent_io_results = run_concurrent_futures_io_benchmark(thread_count, duration, repeats)
        stats = concurrent_io_results['statistics']
        all_results.append({
            'test_name': concurrent_io_results['name'],
            'test_type': 'Concurrent Futures I/O',
            'size_level': SIZE_LEVELS[i],
            'size_value': f"{thread_count} threads, {duration}s/task",
            'python_version': sys.version.split()[0],
            'platform': platform.platform(),
            'architecture': platform.architecture()[0],
            'repeats': repeats,
            'mean_time': stats['mean'],
            'min_time': stats['min'],
            'max_time': stats['max'],
            'std_dev': stats['std_dev'],
            'median_time': stats['median'],
            'timestamp': timestamp
        })
    
    # Save results to CSV
    python_version = sys.version.split()[0].replace('.', '_')
    filename = f"benchmark_results_{python_version}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    save_results_to_csv(all_results, filename)
    
    print("\n" + "=" * 60)
    print("Benchmark completed!")
    print(f"Total tests run: {len(all_results)}")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
