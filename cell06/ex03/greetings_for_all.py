def greetings(name = "noble stranger"):
    if type(name)==str:
        print(f"Hello, {name}.")
    else:
        print("Hello, that is quite a strange name.")
greetings("Guy")
greetings()
greetings(9)