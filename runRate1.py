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

#Accepted Code

t = int(input())

for _ in range(t):
    r1, r2, B = map(int, input().split())

    if B == 0:
        currentRunRate = r2 / 50
    else:
        completedOver = (300 - B) / 6
        currentRunRate = r2 / completedOver

    if B == 0 or r2 > r1:
        requiredRunRate = 0.00
    else:
        runs_needed = (r1 + 1) - r2
        overs_remaining = B / 6
        requiredRunRate = runs_needed / overs_remaining

    print(f"{currentRunRate:.2f} {requiredRunRate:.2f}")

