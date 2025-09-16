import sys

def downcase_it(*words):
    for x in words:
        print(x.lower())

n=0
for x in sys.argv:
    if n!=0:
        downcase_it(x)
    n += 1
if len(sys.argv)==1:
    print("none")