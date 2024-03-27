password= "finally"
nothing_important = "yjidejxqbbemuud"
boo = "abcdefghijklmnopqrstuvwxyz"
user_input=input("What's the password?")
if ("".join([boo[(boo.find(c)+16)%26] for c in user_input]) == nothing_important):
    print("You passed challenge 2")
else:
    print("Et tu, Brute?")