import ctypes

# Load the shared library
lib = ctypes.CDLL("../output/demo.dylib")  # Path to your dylib

# Call the C function
res = lib.hello(50)

print("result from c method: ", res)
