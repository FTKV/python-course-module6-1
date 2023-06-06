with open("vll.txt") as f:
    while True:
        symbol = f.read(2)
        if not symbol:
            break
        print(symbol)

with open("vll.txt") as f:
    while True:
        line = f.readline(4)
        if not line:
            break
        print(line.encode())

with open("vll.txt") as f:
    print(f.readlines())