import os
import sys

print("Files in current directory:")
for f in os.listdir('.'):
    print(f)

print("\nCommand-line arguments:")
for arg in sys.argv:
    print(arg)