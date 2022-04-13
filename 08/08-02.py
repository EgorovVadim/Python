word1 = input()
word2 = input()
bulls = cows = 0
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bulls += 1
    elif word1[i] in word2:
        cows += 1
print(bulls, cows)

