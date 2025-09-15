print("Enter the first number:")
fn = input()
print("Enter the second number:")
sn = input()
ans = int(fn) * int(sn)
print(f"{fn} x {sn} = {ans}")
if ans > 0:
    print("The result is positive.")
elif ans < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")