import sys

if len(sys.argv)!=3:
    print("none")
else:
    fi = sys.argv[1]
    fr = sys.argv[2]
    n=0
    n1=0
    every='no'
    while every == 'no':
        try:
            n=fr.index(fi,n)+1
        except:
            every='yes'
        else:
            n1+=1
    if n==0:
        print("none")
    else:
        print(n1)
    
    