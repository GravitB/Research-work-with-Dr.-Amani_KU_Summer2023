#  The read text function reads the contents of each file, concatenates, and returns the concatenated value.
def read_text_files(file_paths):
    file_contents = []

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            file_contents.append(content)

    return file_contents


# The print files function assigns an index number to each file, prints the contents of the file,
# and inserts a line of dashes to separate it from the next file.
def print_text_files(file_contents):
    for index, content in enumerate(file_contents, start=1):
        print(f"File {index} Content:\n")
        print(content)
        print("\n--------------------------------------\n")


file_paths = ["C:\\files\M1.txt", "C:\\files\M2.txt", "C:\\files\\base.txt"]

# Read text function is called, and it assigns the returned 'file_contents' list to the variable 'contents'
contents = read_text_files(file_paths)
# Print text function is called while passing 'contents' as an argument to print the content of the text files
print_text_files(contents)
