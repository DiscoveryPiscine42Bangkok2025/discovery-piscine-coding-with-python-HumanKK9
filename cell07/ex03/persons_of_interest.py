def famous_births(fname):
    arr=[]
    for x in fname:
        arr.append(fname[x])
    def ysort(y):
        return y['date_of_birth']
    arr.sort(key=ysort)
    for x in arr:
        print(f"{x['name']} is a great scientist born in {x['date_of_birth']}.")

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)