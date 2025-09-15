import sys
try:
    x = sys.argv[2]
except:
    try:
        print(sys.argv[1].lower())
    except:
        print("none")
else:
    print("none")