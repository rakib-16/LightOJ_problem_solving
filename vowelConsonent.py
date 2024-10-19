t = int(input())
for _ in range(t):
    sentence = input().lower()
    vowel =""
    consonant = ""

    for c in sentence:
        if c == 'a' or c == 'e' or c =='i' or c == 'o' or c == 'u':
            vowel += c
        else:
            if c != " ":
                consonant += c

    print(vowel)
    print(consonant)
