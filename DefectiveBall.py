"""
You have 6 balls. 5 balls with same weight and the defective one with different weight.
how can you find the defective ball in minimum steps? using weight machine.
"""
balls = tuple(int(input(f'Enter {i+1} ball Weight : '))for i in range(6))
groupA = balls[0]+balls[1]
groupB = balls[2]+balls[3]
groupC = balls[4]+balls[5]

if groupA==groupB:
    if balls[0]==balls[5]:
        print(f'the 5th ball is defective with weight {balls[4]}')
        print('minimum steps 2')
    else:
        print(f'the 6th ball is defective with weight {balls[5]}')
        print('minimum steps 2')
elif groupA==groupC:
    if balls[0]==balls[2]:
        print(f'the 4th ball is defective with weight {balls[2]}')
        print('minimum steps 3')
    else:
        print(f'the 3rd ball is defective with weight {balls[3]}')
        print('minimum steps 3')
else:
    if balls[2]==balls[0]:
        print(f'the 2nd ball is defective with weight {balls[1]}')
        print('minimum steps 3')
    else:
        print(f'the 1st ball is defective with weight {balls[0]}')
        print('minimum steps 3')