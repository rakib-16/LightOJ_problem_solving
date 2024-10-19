t = int(input())

for _ in range(t):
    wordList = input().split(" ")
    emptyList = []

    for word in wordList:
        ultaWord = word[::-1]
        emptyList.append(ultaWord)

    word_disaster = " ".join(emptyList)
    print(word_disaster)