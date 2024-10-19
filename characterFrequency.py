# from collections import Counter
t = int(input())

for _ in range(t):
    sentence = input()
    char = input()
    if char in sentence:
        freq = sentence.count(char)
        print(f"Occurrence of '{char}' in '{sentence}' = {freq}")
    else:
        print(f"'{char}' is not present")




# T = int(input())
# for i in range(1,T+1):
#     string = input()
#     character = input()
#     if character in string:
#         print("Occurrence of '%s' in '%s' ="%(character,string),string.count(character))
#     else:
#         print("'%s' is not present"%character)
