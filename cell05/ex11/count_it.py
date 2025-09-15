import sys
if len(sys.argv)==1:
    print("none")
else:
    print(f"parameters: {len(sys.argv)-1}")
    i=0
    for x in sys.argv:
        if i==0:
            i+=1
            pass
        else:
            print(f"{x}: {len(x)}")