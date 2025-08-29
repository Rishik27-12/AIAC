try:
    with open("number.txt", "r") as f:
        nums = f.readlines()

    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))

    with open("squares.txt", "w") as f2:
        for sq in squares:
            f2.write(str(sq) + "\n")
    print("Squares written")
except FileNotFoundError:
    print("number.txt not found. Please make sure the file exists in the correct directory.")