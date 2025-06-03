import os
import glob

# Create a sample text file
with open("example.txt", "w") as f:
    f.write("Test content")

# Print working directory
print("Working in:", os.getcwd())

# Find and print .txt files
txt_files = glob.glob("*.txt")
print("Text files in current directory:")
for file in txt_files:
    print(file)
