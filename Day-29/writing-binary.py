import pickle
L1=[10,20,30,40,50]
file=open("bfile.dat","wb")
pickle.dump(L1,file)
print("Data have been written successfully")
