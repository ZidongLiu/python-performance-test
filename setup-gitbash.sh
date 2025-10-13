#!/bin/bash
# Simple setup for 3 Python versions using uv (Git Bash on Windows)
echo "Setting up Python performance testing environments..."

# Create Python 3.13 environment
echo "Creating Python 3.13 environment..."
uv venv --python 3.13 venv-3.13
source venv-3.13/Scripts/activate
uv pip install -e .
deactivate

# Create Python 3.14 environment  
echo "Creating Python 3.14 environment..."
uv venv --python 3.14 venv-3.14
source venv-3.14/Scripts/activate
uv pip install -e .
deactivate

# Create Python 3.14 threadfree environment
echo "Creating Python 3.14 threadfree environment..."
uv venv --python 3.14t venv-3.14-threadfree
source venv-3.14-threadfree/Scripts/activate
uv pip install -e .
deactivate

echo ""
echo "✅ All environments created successfully!"
echo ""
echo "To switch between Python versions:"
echo "  source venv-3.13/Scripts/activate        (Python 3.13)"
echo "  source venv-3.14/Scripts/activate        (Python 3.14)"  
echo "  source venv-3.14-threadfree/Scripts/activate  (Python 3.14 threadfree)"
echo ""
echo "To run the same script with different versions:"
echo "  venv-3.13/Scripts/python.exe example_benchmark.py"
echo "  venv-3.14/Scripts/python.exe example_benchmark.py"
echo "  venv-3.14-threadfree/Scripts/python.exe example_benchmark.py"
echo ""
echo "Press any key to exit..."
read -n 1
