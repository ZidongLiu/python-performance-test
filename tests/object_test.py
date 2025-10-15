"""
Object instantiation and attribute access benchmark tests.
"""

from typing import List, Tuple
from .base_test import BaseBenchmarkTest, time_function


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


class ObjectInstantiationTest(BaseBenchmarkTest):
    """Benchmark test for object instantiation."""
    
    def __init__(self, count: int = 10000, repeats: int = 1):
        """
        Initialize object instantiation test.
        
        Args:
            count: Number of objects to create (default: 10000)
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Object Instantiation ({count:,} objects)", repeats)
        self.count = count
    
    def run_test(self) -> Tuple[List[SimpleClass], float]:
        """
        Run object instantiation benchmark.
        
        Returns:
            Tuple containing (list_of_objects, execution_time)
        """
        return time_function(object_instantiation_test, self.count)
    
    def print_results(self) -> None:
        """Print formatted test results with object count."""
        if not self.results:
            self.execute()
        
        objects = self.results['result']
        print(f"\n{self.results['name']}")
        print(f"   Objects created: {len(objects)}")
        
        if self.repeats == 1:
            print(f"   Time: {self.results['execution_times'][0]:.6f} seconds")
        else:
            stats = self.results['statistics']
            print(f"   Repeats: {self.repeats}")
            print(f"   Mean Time: {stats['mean']:.6f} seconds")
            print(f"   Min Time:  {stats['min']:.6f} seconds")
            print(f"   Max Time:  {stats['max']:.6f} seconds")
            print(f"   Std Dev:   {stats['std_dev']:.6f} seconds")
            print(f"   Median:    {stats['median']:.6f} seconds")


class AttributeAccessTest(BaseBenchmarkTest):
    """Benchmark test for attribute access."""
    
    def __init__(self, objects: List[SimpleClass], repeats: int = 1):
        """
        Initialize attribute access test.
        
        Args:
            objects: List of objects to test attribute access on
            repeats: Number of times to repeat the test (default: 1)
        """
        super().__init__(f"Attribute Access ({len(objects):,} objects)", repeats)
        self.objects = objects
    
    def run_test(self) -> Tuple[int, float]:
        """
        Run attribute access benchmark.
        
        Returns:
            Tuple containing (sum_of_attributes, execution_time)
        """
        return time_function(attribute_access_test, self.objects)
