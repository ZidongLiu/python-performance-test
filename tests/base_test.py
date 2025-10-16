"""
Simple timing utilities for performance testing.
"""

import time
import statistics
from typing import Any, Callable, Dict, List, Tuple


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


def run_benchmark(name: str, func: Callable, *args, repeats: int = 1, **kwargs) -> Dict[str, Any]:
    """
    Run a benchmark function multiple times and return statistical results.
    
    Args:
        name: Name of the benchmark
        func: Function to benchmark
        *args: Positional arguments for the function
        repeats: Number of times to repeat the test (default: 1)
        **kwargs: Keyword arguments for the function
        
    Returns:
        Dictionary containing test results and statistical timing information
    """
    execution_times = []
    test_results = []
    
    # Run the test multiple times
    for i in range(repeats):
        result, execution_time = time_function(func, *args, **kwargs)
        test_results.append(result)
        execution_times.append(execution_time)
    
    # Calculate statistics
    stats = _calculate_statistics(execution_times)
    
    return {
        'name': name,
        'repeats': repeats,
        'result': test_results[0] if test_results else None,  # First result
        'all_results': test_results,
        'execution_times': execution_times,
        'statistics': stats,
        'timestamp': time.time()
    }


def _calculate_statistics(execution_times: List[float]) -> Dict[str, float]:
    """
    Calculate statistical measures for execution times.
    
    Args:
        execution_times: List of execution times
        
    Returns:
        Dictionary containing statistical measures
    """
    if not execution_times:
        return {}
    
    if len(execution_times) == 1:
        return {
            'mean': execution_times[0],
            'min': execution_times[0],
            'max': execution_times[0],
            'std_dev': 0.0,
            'median': execution_times[0]
        }
    
    return {
        'mean': statistics.mean(execution_times),
        'min': min(execution_times),
        'max': max(execution_times),
        'std_dev': statistics.stdev(execution_times) if len(execution_times) > 1 else 0.0,
        'median': statistics.median(execution_times)
    }


def print_benchmark_results(results: Dict[str, Any]) -> None:
    """
    Print formatted benchmark results with statistics.
    
    Args:
        results: Results dictionary from run_benchmark
    """
    print(f"\n{results['name']}")
    print(f"   Result: {results['result']}")
    
    if results['repeats'] == 1:
        print(f"   Time: {results['execution_times'][0]:.6f} seconds")
    else:
        stats = results['statistics']
        print(f"   Repeats: {results['repeats']}")
        print(f"   Mean Time: {stats['mean']:.6f} seconds")
        print(f"   Min Time:  {stats['min']:.6f} seconds")
        print(f"   Max Time:  {stats['max']:.6f} seconds")
        print(f"   Std Dev:   {stats['std_dev']:.6f} seconds")
        print(f"   Median:    {stats['median']:.6f} seconds")

