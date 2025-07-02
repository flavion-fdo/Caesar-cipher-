PText=input("input plain  text ")
Key= int(input("Input key "))
Size= len(PText)
count=0
newword=""

for count in range(Size):
         Let= PText[count:count+1]
         Acs= ord(Let)
         NAcs= Acs+Key
         if Acs>=ord("A") and Acs<=ord("a"):
             if NAcs> ord("Z"):
                 NAcs= NAcs-26
             if NAcs< 65:
                 NAcs= NAcs+26
         else:
             if NAcs> ord("z"):
                 NAcs= NAcs-26
             if NAcs< ord("a"):
                 NAcs= NAcs+26
         newword=newword+chr(NAcs)
print(newword)