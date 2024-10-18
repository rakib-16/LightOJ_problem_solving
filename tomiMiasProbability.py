import math

for _ in range(int(input())):
    n = input().split(" ")
    unique = [word for word in n if word_count[word] == 1]


    for word1 in n:
        for word2 in n:
            if word1 == word2:
                n.remove(word1)

    print(n)
            
        #         sentence.remove(word1)

    # print(sentence)
    # sentence_length = len(n)
    # unique_length = len(sentence)
    

    # print(sentence_length, unique_length)

    # if sentence_length == unique_length:
    #     print(f"1/{math.factorial(sentence_length)}")
    # else : 
    #     duplicateItem = sentence_length - unique_length
    #     probability = math.factorial(sentence_length) / math.factorial(duplicateItem)
    #     print(f"1/{probability}")

    





# t = int(input())
# for _ in range(t):
#     n = input().split()
#     j = math.factorial(len(n))
#     original_list = len(n)
#     remove_duplicates = len(set(n))
#     if original_list == remove_duplicates:
#         print(f"1/{j}")
#     else:
#         duplicateItem = original_list - remove_duplicates
#         print(f"1/{j / duplicateItem}")
   
