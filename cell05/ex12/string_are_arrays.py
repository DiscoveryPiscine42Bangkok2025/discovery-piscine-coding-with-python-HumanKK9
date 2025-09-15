import sys
if len(sys.argv)!=2:
    print("none")
else:
    n=0
    every='no'
    while every == 'no':
        try:
            n=sys.argv[1].index('z',n)+1
        except:
            every='yes'
        else:
            print('z',end='')
    if n==0:
        print("none")
    