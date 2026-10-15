def read_lecture(filename):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    return lines

def search_lecture(lines, keyword):
    keyword_lower = keyword.lower()
    match_count = []
    for x in lines:
        if keyword_lower in x.lower():
            match_count.append(x)
            
    return match_count