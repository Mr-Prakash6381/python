file=open("class1.txt","r")
file.seek(0)
print("Current Position=",file.tell())
print(file.read())
