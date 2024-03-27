import base64

var1 = "secert"
var2 = "notthis"
var3 = "hellothere"
var4 = "bonjour"

def base(a): 
    secert = "MTE1LDEwMSw5OSwxMDEsMTE0LDExNg=="    
    num = ','.join(str(ord(c)) for c in secert)
    enc = num.encode('ascii')
    base2 = base64.b64encode(enc)
    enc2= base2.decode('ascii')
    return enc2
def base2(a):
    secert = "bm90dGhpcw=="
    enc = secert.encode('ascii')
    base2 = base64.b64encode(enc)
    encrypt= base2.decode('ascii')
    return encrypt
def rot13(a):
    boo = "abcdefghijklmnopqrstuvwxyz"
    secert = "uryybgurer" 
    encrypt = "".join([boo[(boo.find(c)+13)%26] for c in a])
    return encrypt
def xor_strings(s) -> bytes:
    secert = "@MLHMWP" 
    return "".join(chr(ord(a) ^ b) for a, b in zip(s, t)).encode('utf8')
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
def tostring(a):
    return a.encode('ascii')

user_input= input("The password:")
if (user_input[0]) == 's':
    userinput = rot13(user_input)
    userinput = rot13(userinput)
    if userinput == var1:
        userinput = base(userinput)
        print("That is not the correct secert")
    else:
        print("That is not the correct secert")
else:
    if user_input[0] == "m":
        print("That is not the correct secert")
    elif user_input[0] == "n":
        var2 = base2(var2)
        userinput = rot13(user_input)
        if userinput[1] == "b":
            userinput = rot13(userinput)
            userinput = base2(userinput) 
            if userinput == var2:
                print("This is the correct secert")
            else:
                userinput = rot13(user_input)
                print("This is not the correct secert")
        else:
            if userinput == var4:
                userinput = base2(userinput)
                print("This is not the correct secert")
            else:
                print("This is not the correct secert")
    else:
        print("This is not the correct secert")