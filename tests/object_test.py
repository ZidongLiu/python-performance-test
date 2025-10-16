"""
Object instantiation and attribute access benchmark tests.
"""

from typing import List
from .base_test import run_benchmark


class SimpleClass:
    """Simple class for object instantiation testing."""
    
    def __init__(self, value: int):
        """
        Initialize SimpleClass instance.
        
        Args:
            value: Integer value to store
        """
        self.value = value
        self.name = f"object_{value}"
        self.data = {"id": value, "active": True}


def object_instantiation_test(count: int) -> list[SimpleClass]:
    """
    Test object instantiation performance.
    
    Args:
        count: Number of objects to create
        
    Returns:
        list of created SimpleClass objects
    """
    objects = []
    for i in range(count):
        obj = SimpleClass(i)
        objects.append(obj)
    return objects


def attribute_access_test(objects: list[SimpleClass]) -> int:
    """
    Test attribute access performance.
    
    Args:
        objects: list of SimpleClass objects
        
    Returns:
        Sum of accessed attribute values
    """
    total = 0
    for obj in objects:
        total += obj.value
        
    return total


def run_object_instantiation_benchmark(count: int = 10000, repeats: int = 1) -> dict:
    """
    Run object instantiation benchmark.
    
    Args:
        count: Number of objects to create (default: 10000)
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Object Instantiation ({count:,} objects)", 
                          object_instantiation_test, count, repeats=repeats)
    return results


def run_attribute_access_benchmark(objects: List[SimpleClass], repeats: int = 1) -> dict:
    """
    Run attribute access benchmark.
    
    Args:
        objects: List of objects to test attribute access on
        repeats: Number of times to repeat the test (default: 1)
        
    Returns:
        Dictionary containing benchmark results
    """
    results = run_benchmark(f"Attribute Access ({len(objects):,} objects)", 
                          attribute_access_test, objects, repeats=repeats)
    return results


def print_object_instantiation_results(results: dict) -> None:
    """Print formatted object instantiation test results with object count."""
    objects = results['result']
    print(f"\n{results['name']}")
    print(f"   Objects created: {len(objects)}")
    
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
