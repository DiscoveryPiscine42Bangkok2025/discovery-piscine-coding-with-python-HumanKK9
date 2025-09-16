import sys

if len(sys.argv)==1:
    print("none")

def shrink(nonshrink):
    i=0
    for x in nonshrink:
        print(x,end="")
        i+=1
        if i>=8:
            print()
            break
    #alternatively print(nonshrink[slice(8)])

def enlarge(unlarge):
    i=0
    while i<8:
        try:
            print(unlarge[i],end="")
        except:
            print('Z',end='')
        i+=1
    print()

fc=0
for x in sys.argv:
    if fc==0:
        fc=1
    elif len(x) < 8:
        enlarge(x)
    else:
        shrink(x)