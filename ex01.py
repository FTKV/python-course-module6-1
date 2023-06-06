# file = open("vll.txt","r+")
# print(file)
# file.close()

result = []
for _ in range(10):
        result.append("Hello")

with open("vll.txt", "w") as f:
    f.write("\n".join(result))