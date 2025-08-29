with open("helloworld.txt", "r") as f:

    # Cannot write to a file opened in read mode. Use read() instead if you want to read the file.
    content = f.read()
    print(content)