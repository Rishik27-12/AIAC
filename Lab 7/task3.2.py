try:
    with open("input.txt", "r") as infile:
        data = infile.readlines()
    with open("output.txt", "w") as outfile:
        for line in data:
            outfile.write(line.upper())
    print("processing done")
except FileNotFoundError:
    print("input.txt not found. Please make sure the file exists in the correct directory.")