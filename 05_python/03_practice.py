with open("05_python/03_practice.txt", "r")as f:
    data = f.readline()
    print(data)

    data = f.readline()
    print(data)

    data = f.readline()
    print(data)

# now with data variable-->>
data = True
line = 1
word = "python"

with open("05_python/03_practice.txt", "r")as f:
    while data:
        data = f.readline()
        if(word in data):
            print(f"{word} found at line {line}")
            break

        line += 1
