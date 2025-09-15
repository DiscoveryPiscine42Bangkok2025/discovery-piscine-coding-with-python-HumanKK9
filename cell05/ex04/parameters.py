import sys
things= []
n=0
for x in sys.argv:
    if n!=0:
        things.append(x)
    n += 1
print(f"Number of parameters: {len(things)}.")