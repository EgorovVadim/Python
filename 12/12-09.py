char = input().lower()
line = input().split()
for word in line:
    if char in word.lower():
        print(word)
