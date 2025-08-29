from typing import TextIO

with open("input.txt", "r") as src:  # type: TextIO
    with open("output.txt", "w") as dst:  # type: TextIO
        for line in src:
            dst.write(line.upper())

print("Processing done")

 
