doc = ""
toFind = ""


def is_maj(c):
    if 65 <= ord(c) <= 90:
        return True
    else:
        return False


with open('level4text', 'r') as file:
    # Iterate through the lines
    for line in file:
        for char in line:
            doc += char

    for i in range(3, len(doc) - 4):
        if not is_maj(doc[i]):
            if not is_maj(doc[i - 4]) and not is_maj(doc[i + 4]):
                if is_maj(doc[i - 3]) and is_maj(doc[i - 2]) and is_maj(doc[i - 1]):
                    if is_maj(doc[i + 3]) and is_maj(doc[i + 2]) and is_maj(doc[i + 1]):
                        toFind += doc[i]

print(toFind)
