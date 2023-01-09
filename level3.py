dict = {}

with open('level3text.txt', 'r') as file:
    # Iterate through the lines
    for line in file:
        for char in line:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

print(dict)

toFind = ""
with open('level3text.txt', 'r') as file:
    for line in file:
        for char in line:
            if 97 <= ord(char) <= 122:
                toFind += char

print(toFind)
