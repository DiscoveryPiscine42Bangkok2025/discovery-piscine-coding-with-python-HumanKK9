import sys
if len(sys.argv)!=2:
    print("none")
else:
    gpara = sys.argv[1]
    rpara = input("What was the parameter? ")
    if rpara == gpara:
        print("Good job!")
    else:
        print("Nope, sorry...")