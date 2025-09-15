import sys
try:
    x = sys.argv[2]
except:
    try:
        print(sys.argv[1].upper())
    except:
        print("none")
else:
    print("none")