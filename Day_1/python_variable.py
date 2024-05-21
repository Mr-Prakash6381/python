a=10 #An integer assignment
b=3.14 # A floating point
c="Prakash" # A string
print(a)
print(b)
print(c)
print("\n")
# Object Reference
print(type("Prakash"))
print(type("P"))
a=11
b=1.11
c="p"
print(type(c))
print(type(a))
print(type(b))
print("\n")
# Object Identitfy
print(id(a))
print(id(b))
print(id(c))
print("\n")
# Multiple Assignment
  # 1 Assigning single value to multiple variables
a=b=c=20
print(a)
print(b)
print(c)

print("\n")

 # 2 Assigning muultiple values to multiple variable

a,b,c=5,10,15
print(a)
print(b)
print(c)

print("\n")


# Python Variable types

    # 1 Local Variable

    # 2 Global Variable

    
# local variable

#declaring a function

def add():
    a=10
    b=12
    c=a+b
    print("c=",c)

# calling a function
add()

# Global Variable

h=10
def disp():
    global h
    print("Before H=",h)
    h="Welcome to css"
    print(h)

disp()
print(h)

# Delete a variable

a=10
print(a)
#del a
print(a)

#print single and multiple varibale in python

  #printing single varibale
a=10
print(a)

  #Printing multiple variable
a=10
b=20
print(a,b)





















    
