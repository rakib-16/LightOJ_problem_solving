for _ in range(int(input())):
    a, b = map(int, input().split())
    count = 0


    for i in range(a, b + 1):
        k = int(i/2) + 1

        for j in range(2, k):
            if i % j == 0 : 
                break
            else :
                if j+1 == k:
                    count += 1
        
    print(count)
    

            


    
            
            # print
            # print(j)
            # if i%j == 0 :
            #     break
            # else:
            #     count += 1


    # print(count)
