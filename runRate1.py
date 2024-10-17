# t = int(input())

# for _ in range(t):
#     n = input()
#     opponentRun = int(n.split(" ")[0])
#     batsmanRun = int(n.split(" ")[1])
#     remainingBall = int(n.split(" ")[2])

#     completedOver = (300 - remainingBall) / 6
#     currentRunRate = batsmanRun / completedOver
#     RequiredRunRate = ((opponentRun + 1) - batsmanRun) / (remainingBall / 6)

#     print(f"{currentRunRate:.2f} {RequiredRunRate:.2f}")

# Number of test cases


T = int(input())

while T > 0:
    # Read inputs
    r1, r2, B = map(int, input().split())
    
    # Calculate balls played
    ball_played = 300 - B

    # Calculate current run rate and asking run rate
    current_rr = (r2 / ball_played) * 6
    asking_rr = ((r1 - r2 + 1) / B) * 6

    # Print results with two decimal places
    print(f"{current_rr:.2f} {asking_rr:.2f}")
    
    T -= 1
