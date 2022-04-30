# Rail Fence cipher encryption
plaintext=input("enter the plain text : ")
key=int(input("enter the key value : "))
text=plaintext.upper()
matrix=[[" " for x in range(len(plaintext))] for y in range(key)]
flag=0
row=0
for i in range(len(text)):
  matrix[row][i]=text[i]
  if row==0:
    flag=0
  elif row==key-1:
    flag=1
  if flag==0:
    row+=1
  else:
    row-=1
for i in range(key):
    "".join(matrix[i])
ciphertext=[]
for i in range(key):
    for j in range(len(text)):
        if matrix[i][j]!=' ':
            ciphertext.append(matrix[i][j])
cipher="".join(ciphertext)
print("Cipher Text: ",cipher)
