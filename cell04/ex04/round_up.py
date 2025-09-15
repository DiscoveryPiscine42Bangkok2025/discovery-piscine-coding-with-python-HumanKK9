nr=input("Give me a number: ")
if float(nr).is_integer() == True:
    print(int(float(nr)))
else:
    print(int(float(nr)-float(nr)%1+1))