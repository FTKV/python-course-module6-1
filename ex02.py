result = ""
with open("vll.txt") as f:
    f.seek(7)
    result = f.read(20)

print(result)
for i in result:
    print(ord(i))