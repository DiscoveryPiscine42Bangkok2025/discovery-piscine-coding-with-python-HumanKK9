def array_of_names(names):
    aon=[]
    for x in names:
        #x is first, names[x] is second
        aon.append(f"{x[0:1].upper()}{x[1:]} {names[x][0:1].upper()}{names[x][1:]}")

    return aon


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))