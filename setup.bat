@echo off
REM Simple setup for 3 Python versions using uv (Windows CMD)
echo Setting up Python performance testing environments...

REM Create Python 3.13 environment
echo Creating Python 3.13 environment...
uv venv --python 3.13 venv-3.13
call venv-3.13\Scripts\activate.bat
uv pip install -e .
call deactivate

REM Create Python 3.14 environment  
echo Creating Python 3.14 environment...
uv venv --python 3.14 venv-3.14
call venv-3.14\Scripts\activate.bat
uv pip install -e .
call deactivate

REM Create Python 3.14 threadfree environment
echo Creating Python 3.14 threadfree environment...
uv venv --python 3.14t venv-3.14-threadfree
call venv-3.14-threadfree\Scripts\activate.bat
uv pip install -e .
call deactivate

echo.
echo ✅ All environments created successfully!
echo.
echo To switch between Python versions:
echo   venv-3.13\Scripts\activate.bat        (Python 3.13)
echo   venv-3.14\Scripts\activate.bat        (Python 3.14)  
echo   venv-3.14-threadfree\Scripts\activate.bat  (Python 3.14 threadfree)
echo.
echo To run the same script with different versions:
echo   venv-3.13\Scripts\python.exe example_benchmark.py
echo   venv-3.14\Scripts\python.exe example_benchmark.py
echo   venv-3.14-threadfree\Scripts\python.exe example_benchmark.py
echo.
echo Press any key to exit...
pause >nul
