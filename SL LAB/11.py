mystrings=["i am going home at 12","1 live 12 kms away ","I am hungry","Give me a packet","Dosa for Rs 14"]
print(mystrings)

for i in range (len(mystrings)):
       if i%2==0:
            print("Index at",i,mystrings[i])
for i in range (len(mystrings)):
       if i%3==0:
            mystrings[i]=mystrings[i].upper()
            print(mystrings)
for i in range (len(mystrings)):
       mystrings[i]=" ".join(reversed(mystrings[i].split()))
       print(mystrings)
num=[]
for i in range (len(mystrings)):
       for s in mystrings[i].split():
               if s.isdigit():
                   num.append(s)
                   print(num)