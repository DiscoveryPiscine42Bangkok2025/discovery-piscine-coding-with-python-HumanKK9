aig = [2, 8, 9, 48, 8, 22, -12, 2]
print(aig)
na=[]
for x in aig:
    na.append(x+2)
nna=[]
for x in na:
    if x>5:
        nna.append(x)
print(nna)