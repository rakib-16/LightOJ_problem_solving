from collections import Counter

case = int(input())
for t in range(case):
    sentence = input()
    freq = Counter(sentence)
    for i in freq:
        print(i , "=", freq[i])

    if t + 1 != case:
        print()