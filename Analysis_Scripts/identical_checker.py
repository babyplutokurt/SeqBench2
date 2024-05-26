def files_are_identical(file1, file2, chunk_size=1024):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            chunk1 = f1.read(chunk_size)
            chunk2 = f2.read(chunk_size)

            if chunk1 != chunk2:
                return False

            if not chunk1:  # End of file
                return True

# Example usage
file1 = 'path/to/first/file.txt'
file2 = 'path/to/second/file.txt'

if files_are_identical(file1, file2):
    print("The files are identical.")
else:
    print("The files are different.")
