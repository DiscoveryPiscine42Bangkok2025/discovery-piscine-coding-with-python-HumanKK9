import sys
if len(sys.argv)!=3:
    print("none")
else:
    arr=[]
    if sys.argv[1] > sys.argv[2]:
        b=int(sys.argv[1])
        a=int(sys.argv[2])
    else:
        a=int(sys.argv[1])
        b=int(sys.argv[2])
    for x in range(a,b+1):
        arr.append(x)
    print(arr)