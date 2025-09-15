import sys
things= []
n=0
for x in sys.argv:
    if n!=0:
        things.append(x)
    n += 1
things.reverse()
if len(things)<2:
    print("none")
else:
    for x in things:
        print(x)