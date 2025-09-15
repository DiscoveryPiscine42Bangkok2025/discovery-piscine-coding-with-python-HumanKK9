print("Enter a number less than 25")
ni = input()
n = int(ni)
if n > 25:
    print("Error")
else:
    for x in range(n, 26):
        print(f"Inside the loop, my variable is {x}")
 