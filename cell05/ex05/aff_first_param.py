import sys
things= []
n=0
for x in sys.argv:
    if n!=0:
        things.append(x)
    n += 1
first='yes'
for x in things:
    if type(x) == str and first == 'yes':
        print(x)
        first='no'
if first == 'yes':
    print("none")