# Python Performance Testing

A comprehensive benchmarking suite to evaluate and compare Python performance across different versions: Python 3.13, Python 3.14, and Python 3.14 threadfree.

## Overview

This repository contains performance tests designed to measure and analyze the execution characteristics of different Python versions. The benchmarks cover various computational patterns including CPU-intensive tasks, memory operations, and language feature performance.

## Quick Setup with uv

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package and environment management.

### Installation

1. **Install uv** (if not already installed):

   ```cmd
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Set up all Python environments**:

   ```cmd
   REM For Windows CMD
   setup.bat

   REM For Git Bash on Windows
   bash setup-gitbash.sh
   ```

### Manual Setup (Alternative)

If you prefer to set up manually:

```cmd
REM Create Python 3.13 environment
uv venv --python 3.13 venv-3.13
venv-3.13\Scripts\activate.bat
uv pip install -e .
deactivate

REM Create Python 3.14 environment
uv venv --python 3.14 venv-3.14
venv-3.14\Scripts\activate.bat
uv pip install -e .
deactivate

REM Create Python 3.14 threadfree environment
uv venv --python 3.14t venv-3.14-threadfree
venv-3.14-threadfree\Scripts\activate.bat
uv pip install -e .
deactivate
```

## Switching Between Python Versions

### Windows CMD

```cmd
REM Switch to Python 3.13
venv-3.13\Scripts\activate.bat

REM Switch to Python 3.14
venv-3.14\Scripts\activate.bat

REM Switch to Python 3.14 threadfree
venv-3.14-threadfree\Scripts\activate.bat
```

### Git Bash on Windows

```bash
# Switch to Python 3.13
source venv-3.13/Scripts/activate

# Switch to Python 3.14
source venv-3.14/Scripts/activate

# Switch to Python 3.14 threadfree
source venv-3.14-threadfree/Scripts/activate
```

## Running Scripts with Different Python Versions

You can run the same script with different Python versions without switching environments:

### Windows CMD

```cmd
venv-3.13\Scripts\python.exe benchmark.py
venv-3.14\Scripts\python.exe benchmark.py
venv-3.14-threadfree\Scripts\python.exe benchmark.py
```

### Git Bash on Windows

```bash
venv-3.13/Scripts/python.exe benchmark.py
venv-3.14/Scripts/python.exe benchmark.py
venv-3.14-threadfree/Scripts/python.exe benchmark.py
```

## Test Plan

The following benchmarks are implemented to evaluate different aspects of Python performance:

1. **Fibonacci Sequence Calculation** - CPU-intensive recursive algorithm to test recursion performance and stack management
2. **Bubble Sort Algorithm** - CPU-intensive iterative algorithm to test loop performance and array operations
3. **list/Dict/Set Comprehensions** - Memory allocation and iteration patterns for data structure operations
4. **Function Call Overhead** - Repeated function calls to measure call stack performance and overhead
5. **Exception Handling** - try/except/finally clause performance to test error handling mechanisms
6. **Object Instantiation** - Class object creation with varying complexity:
   - No attributes
   - Simple attributes
   - Nested complex data attributes
7. **Attribute Access** - Object attribute access patterns (e.g., `object.attribute`)

## Methodology

Each benchmark is designed to:

- Measure execution time using high-precision timing
- Track memory usage and allocation patterns
- Generate statistical analysis of performance differences
- Provide reproducible results across different Python versions

## Project Structure

```
python-performance-test/
├── venv-3.13/                        # Python 3.13 virtual environment
├── venv-3.14/                        # Python 3.14 virtual environment
├── venv-3.14-threadfree/             # Python 3.14 threadfree virtual environment
├── benchmark.py              # Example benchmark script
├── setup.bat                         # Windows CMD setup script
├── setup-gitbash.sh                  # Git Bash setup script
├── pyproject.toml                    # Project configuration
└── README.md
```

## Example Usage

1. **Set up the project:**

   ```cmd
   REM For Windows CMD
   setup.bat

   REM For Git Bash on Windows
   bash setup-gitbash.sh
   ```

2. **Run the same script with different Python versions:**

   ```cmd
   REM Windows CMD
   venv-3.13\Scripts\python.exe benchmark.py
   venv-3.14\Scripts\python.exe benchmark.py
   venv-3.14-threadfree\Scripts\python.exe benchmark.py
   ```

   ```bash
   # Git Bash on Windows
   venv-3.13/Scripts/python.exe benchmark.py
   venv-3.14/Scripts/python.exe benchmark.py
   venv-3.14-threadfree/Scripts/python.exe benchmark.py
   ```

3. **Compare performance results** across the different Python versions.

## Requirements

- **uv** - Fast Python package manager
- **Python 3.13+** - Base Python version
- **Virtual environment support** - For isolated testing environments
- **Performance measurement tools** - timeit, cProfile, memory_profiler

## Troubleshooting

### Common Issues

1. **uv not found**: Make sure uv is installed and in your PATH
2. **Python version not available**: Ensure the Python version is installed on your system
3. **Virtual environment creation fails**: Check disk space and permissions
4. **Dependencies installation fails**: Verify internet connection and try updating uv

### Getting Help

- Check the [uv documentation](https://github.com/astral-sh/uv)
- Review the project's issue tracker
- Ensure all system requirements are met
