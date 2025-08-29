f = open("numbers.txt","r")
nums = f.readlines()

squares = []
for n in nums:
    n = n.strip()
    if n.isdigit():
        squares.append(int(n) * int(n))

f2 = open("squares.txt","w")
for sq in squares:
    f2.write(str(sq) + "\n")
print("Squares written")
f2.close()