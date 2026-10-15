from lecture_utils import read_lecture, search_lecture

print("The start of Program ")


try:
    lines = read_lecture("missing.txt")

except FileNotFoundError:
    print("Error: file not found")

else:
    print("File loaded successfully")
    matches = search_lecture(lines, "python")
    print("Total matching lines:", len(matches))

    if len(matches) == 0:
        print("no matching lines")
        
    for x in matches :
        print(x.rstrip("\n"))


