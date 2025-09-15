n1r = 0
n2r = 0
n1= int(n1r)
n2= int(n2r)
while n1 <= 10:
    print(f"Table de {n1}: ",end="")
    while n2 <= 10:
        print(f"{n1*n2} ",end="")
        n2 += 1
    print()
    n1 += 1
    n2=0