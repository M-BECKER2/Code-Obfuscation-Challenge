import base64

carrot = 'MTA0LDEwMSwxMDgsMTA4LDExMSw0NCwzMiwxMTYsMTA0LDEwMSwzMiwzNA==' 
onion = 'MzQsMzIsMTEyLDk3LDExNSwxMTUsOTksMTExLDEwMCwxMDE=' 
potato = 'MTA1LDExNSwzMiwxMDUsMTEwLDMyLDExMywxMTcsMTExLDExNiwxMDEsMTE1' 
bean = 'OTksOTcsMTEwLDExNiw5NSw5OSw5NywxMTYsOTksMTA0LDk1LDEwOSwxMDE=' 

user_input = input("The passcode, please: ")
num = ','.join(str(ord(c)) for c in user_input)
carrt5 = num.encode('ascii')
base2 = base64.b64encode(carrt5)
beans= base2.decode('ascii')

if( carrot + bean + onion + potato) == ( carrot + beans + onion + potato):
    print("correct, you have completed challenge 1")
else:
    print("incorrect, please try again")
  
