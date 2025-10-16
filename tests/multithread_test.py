"""
Multi-threading performance benchmark tests.
"""

import threading
import time
import concurrent.futures
from typing import List
from .base_test import run_benchmark


def cpu_intensive_task(task_id: int, iterations: int) -> int:
    """
    CPU-intensive task for multi-threading test.
    
    Args:
        task_id: Unique identifier for the task
        iterations: Number of iterations to perform
        
    Returns:
        Sum of calculations
    """
    result = 0
    for i in range(iterations):
        result += i * task_id + (i ** 2) % 1000
    return result


def io_intensive_task(task_id: int, duration: float) -> int:
    """
    I/O-intensive task simulation for multi-threading test.
    
    Args:
        task_id: Unique identifier for the task
        duration: Duration to simulate I/O operations
        
    Returns:
        Task ID
    """
    time.sleep(duration)
    return task_id


def multithread_cpu_test(num_threads: int, iterations_per_thread: int) -> List[int]:
    """
    Test multi-threading performance with CPU-intensive tasks.
    
    Args:
        num_threads: Number of threads to spawn
        iterations_per_thread: Number of iterations per thread
        
    Returns:
        List of results from all threads
    """
    results = []
    threads = []
    
    def worker(thread_id: int):
        result = cpu_intensive_task(thread_id, iterations_per_thread)
        results.append(result)
    
    # Create and start threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return results


def multithread_io_test(num_threads: int, duration_per_task: float) -> List[int]:
    """
    Test multi-threading performance with I/O-intensive tasks.
    
    Args:
        num_threads: Number of threads to spawn
        duration_per_task: Duration of each I/O task
        
    Returns:
        List of results from all threads
    """
    results = []
    threads = []
    
    def worker(thread_id: int):
        result = io_intensive_task(thread_id, duration_per_task)
        results.append(result)
    
    # Create and start threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    return results


def concurrent_futures_cpu_test(num_threads: int, iterations_per_thread: int) -> List[int]:
    """
    Test concurrent.futures performance with CPU-intensive tasks.
    
    Args:
        num_threads: Number of threads to spawn
        iterations_per_thread: Number of iterations per thread
        
    Returns:
        List of results from all threads
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(cpu_intensive_task, i, iterations_per_thread)
            for i in range(num_threads)
        ]
        results = [future.result() for future in futures]
    
    return results


def concurrent_futures_io_test(num_threads: int, duration_per_task: float) -> List[int]:
    """
    Test concurrent.futures performance with I/O-intensive tasks.
    
    Args:
        num_threads: Number of threads to spawn
        duration_per_task: Duration of each I/O task
        
    Returns:
        List of results from all threads
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [
            executor.submit(io_intensive_task, i, duration_per_task)
            for i in range(num_threads)
        ]
        results = [future.result() for future in futures]
    
    return results


def run_multithread_cpu_benchmark(num_threads: int = 4, iterations_per_thread: int = 100000, repeats: int = 1) -> dict:
    """
    Run multi-threading CPU benchmark.
    
    Args:
        num_threads: Number of threads to spawn (default: 4)
        iterations_per_thread: Number of iterations per thread (default: 100000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Multi-thread CPU ({num_threads} threads, {iterations_per_thread:,} iter/thread)", 
                          multithread_cpu_test, num_threads, iterations_per_thread, repeats=repeats)
    return results


def run_multithread_io_benchmark(num_threads: int = 4, duration_per_task: float = 0.01, repeats: int = 1) -> dict:
    """
    Run multi-threading I/O benchmark.
    
    Args:
        num_threads: Number of threads to spawn (default: 4)
        duration_per_task: Duration of each I/O task in seconds (default: 0.01)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Multi-thread I/O ({num_threads} threads, {duration_per_task}s/task)", 
                          multithread_io_test, num_threads, duration_per_task, repeats=repeats)
    return results


def run_concurrent_futures_cpu_benchmark(num_threads: int = 4, iterations_per_thread: int = 100000, repeats: int = 1) -> dict:
    """
    Run concurrent.futures CPU benchmark.
    
    Args:
        num_threads: Number of threads to spawn (default: 4)
        iterations_per_thread: Number of iterations per thread (default: 100000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Concurrent Futures CPU ({num_threads} threads, {iterations_per_thread:,} iter/thread)", 
                          concurrent_futures_cpu_test, num_threads, iterations_per_thread, repeats=repeats)
    return results


def run_concurrent_futures_io_benchmark(num_threads: int = 4, duration_per_task: float = 0.01, repeats: int = 1) -> dict:
    """
    Run concurrent.futures I/O benchmark.
    
    Args:
        num_threads: Number of threads to spawn (default: 4)
        duration_per_task: Duration of each I/O task in seconds (default: 0.01)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Concurrent Futures I/O ({num_threads} threads, {duration_per_task}s/task)", 
                          concurrent_futures_io_test, num_threads, duration_per_task, repeats=repeats)
    return results
