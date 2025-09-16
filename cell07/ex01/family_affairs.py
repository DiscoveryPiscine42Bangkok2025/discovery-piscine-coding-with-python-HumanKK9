def find_the_redheads(fam):
    redname=[]
    for x in fam:
        #x is first, fam[x] is second
        if fam[x]=="red":
            redname.append(x)
    return redname

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))