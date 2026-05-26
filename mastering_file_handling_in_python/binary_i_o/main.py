# Write Python code to open a file named "data.bin" in binary write mode and write the bytes b'PythonRocks!' to it.
data_to_write = b'PythonRocks!'
# Write your code here
with open("data.bin", "wb") as file:
    file.write(data_to_write)
# Then, open the same file in binary read mode, read the contents, and store them in a variable named "read_bytes".
with open("data.bin", "rb") as file:
    read_bytes = file.read()
# Write your code here
print(read_bytes)