#!/usr/bin/env python3
"""
Example script that demonstrates running the same code across different Python versions.
This script can be executed with any of the three Python versions to show performance differences.
"""

import sys
import time
import platform
from typing import List


def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def bubble_sort(arr: List[int]) -> List[int]:
    """Sort a list using bubble sort algorithm."""
    n = len(arr)
    arr = arr.copy()  # Don't modify the original
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


def list_comprehension_test(size: int) -> List[int]:
    """Test list comprehension performance."""
    return [i * i for i in range(size)]


def function_call_overhead_test(iterations: int) -> int:
    """Test function call overhead."""
    def simple_function(x: int) -> int:
        return x + 1
    
    result = 0
    for i in range(iterations):
        result += simple_function(i)
    
    return result


def exception_handling_test(iterations: int) -> int:
    """Test exception handling performance."""
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


class SimpleClass:
    """Simple class for object instantiation testing."""
    def __init__(self, value: int):
        self.value = value
        self.name = f"object_{value}"
        self.data = {"id": value, "active": True}


def object_instantiation_test(count: int) -> List[SimpleClass]:
    """Test object instantiation performance."""
    objects = []
    for i in range(count):
        obj = SimpleClass(i)
        objects.append(obj)
    return objects


def attribute_access_test(objects: List[SimpleClass]) -> int:
    """Test attribute access performance."""
    total = 0
    for obj in objects:
        total += obj.value
        total += len(obj.name)
        total += obj.data["id"]
    return total


def run_benchmarks() -> None:
    """Run all benchmarks and display results."""
    print("=" * 60)
    print("Python Performance Test Results")
    print("=" * 60)
    print(f"Python Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.architecture()}")
    print("=" * 60)
    
    # Test 1: Fibonacci (small number to avoid long execution)
    print("\n1. Fibonacci Sequence (n=25)")
    start_time = time.perf_counter()
    fib_result = fibonacci(25)
    end_time = time.perf_counter()
    print(f"   Result: {fib_result}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 2: Bubble Sort
    print("\n2. Bubble Sort (1000 elements)")
    test_array = list(range(1000, 0, -1))  # Reverse sorted array
    start_time = time.perf_counter()
    sorted_array = bubble_sort(test_array)
    end_time = time.perf_counter()
    print(f"   First 5 elements: {sorted_array[:5]}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 3: List Comprehension
    print("\n3. List Comprehension (100,000 elements)")
    start_time = time.perf_counter()
    comp_result = list_comprehension_test(100000)
    end_time = time.perf_counter()
    print(f"   Length: {len(comp_result)}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 4: Function Call Overhead
    print("\n4. Function Call Overhead (100,000 calls)")
    start_time = time.perf_counter()
    call_result = function_call_overhead_test(100000)
    end_time = time.perf_counter()
    print(f"   Result: {call_result}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 5: Exception Handling
    print("\n5. Exception Handling (10,000 iterations)")
    start_time = time.perf_counter()
    exc_result = exception_handling_test(10000)
    end_time = time.perf_counter()
    print(f"   Result: {exc_result}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 6: Object Instantiation
    print("\n6. Object Instantiation (10,000 objects)")
    start_time = time.perf_counter()
    objects = object_instantiation_test(10000)
    end_time = time.perf_counter()
    print(f"   Objects created: {len(objects)}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    # Test 7: Attribute Access
    print("\n7. Attribute Access (10,000 objects)")
    start_time = time.perf_counter()
    attr_result = attribute_access_test(objects)
    end_time = time.perf_counter()
    print(f"   Result: {attr_result}")
    print(f"   Time: {end_time - start_time:.6f} seconds")
    
    print("\n" + "=" * 60)
    print("Benchmark completed!")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
