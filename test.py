# test_serial.py
import sys
print(f"Python version: {sys.version}")
print(f"Python path: {sys.executable}")

try:
    import serial
    print(f"Pyserial version: {serial.__version__}")
    print(f"Serial module location: {serial.__file__}")
    
    # Try to create a Serial object
    test_serial = serial.Serial
    print("Successfully imported Serial class")
    
except ImportError as e:
    print(f"Import Error: {e}")
except Exception as e:
    print(f"Other Error: {e}")

print("\nPython path:")
for path in sys.path:
    print(path)