

for _ in range(int(input())):
    sentence = input().lower()
    vowel = 0
    for c in sentence:
        if c == 'a' or c == 'e' or c =='i' or c == 'o' or c == 'u':
            vowel += 1
    print(f"Number of vowels = {vowel}") 

    