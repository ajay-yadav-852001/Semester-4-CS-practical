TEXT=input("enter the text : ")
KEY=int(input("enter the key value : "))
newtext=""
for i in TEXT:
    if i.isupper():
        newtext+=chr((ord(i)+KEY-65)%26+65)
    elif (ord(i)==32):
        newtext+=chr(ord(i))
    else:
        newtext+=chr((ord(i)+KEY-97)%26+97)
print("Cipher Text : ",newtext)
