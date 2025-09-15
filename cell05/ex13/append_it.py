import sys
if len(sys.argv)==1:
    print("none")
else:
    i=0
    for x in sys.argv:
        ism=-1
        if i==0:
            i=1
            pass
        elif x.find('ism') == -1:
            x=x+"ism"
            print(x)
            #alternatively just print(f"{x}ism")