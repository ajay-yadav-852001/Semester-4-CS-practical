# Ceaser Cipher Decryption 
Cipher_text=input("enter the encrypted text : ")
key =int(input("enter tyhe key value : "))
Plain_text=""
for i in Cipher_text:
    if i.isupper():
        Plain_text+=chr((ord(i)-key-65)%26+65)
    elif(ord(i)==32):
        Plain_text+=chr(ord(i))
    else:
        Plain_text+=chr((ord(i)-key-97)%26+97)
print("Plain Text : ",Plain_text)
