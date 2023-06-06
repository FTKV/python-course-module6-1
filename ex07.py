with open ("test.mp3", "rb") as f:
    data = f.readlines()
    print(data[:1])