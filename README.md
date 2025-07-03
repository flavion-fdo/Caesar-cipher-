#python code 
PText=input("input plain  text ")
Key= int(input("Input key "))
Size= len(PText)
count=0
newword=""

for i in range(Size):
    Let= PText[count:count+1]
    if Let>="A" and Let<= "Z":
        Max=ord("Z")
        Min=ord("A")
    if Let>="a" and Let<= "z":
         Max=ord("a")
         Min=ord("z")
    Asc=ord(Let)
    NAcs= Asc+Key
    if Key>0:
        if NAsc>Max:
            NAcs= NAcs-26
    elif Key<0: 
        if NAsc>Min:
            NAcs= NAcs+26
    newword=newword+chr(NAcs)
print(newword)

            
             
