def encrypt(a):
    str1=""
    txt = input("Enter text::")
    for j in txt:
        if(j=='z'):
            #print('a')
            str1=str1+'a'
        elif(j==' '):
            str1=str1+' '
        else:
            for i in range(0,26):
                if(a[i]==j):
                    #print(a[i+1])
                    str1=str1+(a[i+1])
    print("Your Encrypted Code is::",str1)
def decrypt(a):
    str1=""
    txt1 = input("Enter Encrypted Code::")
    for j in txt1:
        if(j=='a'):
            #print('z')
            str1=str1+'z'
        elif(j==' '):
            str1=str1+' '
        else:
            for i in range(0,26):
                if(a[i]==j):
                    #print(a[i+1])
                    str1=str1+(a[i-1])
    print("Your Decrypted Code is::",str1)
a=[]
str="abcdefghijklmnopqrstuvwxyz"
for i in str:
    a.append(i)
while(True):
    ch=int(input("1.Encryption\n2.Decryption\n3.Exit\nEnter your choice::"))
    if(ch==1):
        encrypt(a)
    elif(ch==2):
        decrypt(a)
    else:
        break
