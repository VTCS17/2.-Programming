kids = open("Samunames.txt","r+")
#print(kids.readline())
#print(kids.readlines()[2])
for kid in kids.readlines():
    print(kid)
kids.close()