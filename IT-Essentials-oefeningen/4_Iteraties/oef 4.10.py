hoogte = int(input("hoogte: "))

for i in range(hoogte,0,-1):
    for j in range(0,i):
        print("@ ", end="")
    print()