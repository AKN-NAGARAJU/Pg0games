WIDTH=400
HEIGHT=400
abba=[]
total=0

file=open("questions2.txt","r")
for f in file:
    abba.append(f)
file.close()
for a in abba:
    total=total+int(a)
print(total)
print(abba)