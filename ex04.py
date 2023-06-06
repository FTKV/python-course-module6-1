with open("vll.txt") as f:
    while True:
        chunk = f.read(1)
        if not chunk:
            break
        print(f.tell(), chunk)