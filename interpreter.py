expression=input('Expression:').split(" ")

x,y,z = expression

X=float(x)
Z=float(z)

if y=="+":
    print(X+Z)
elif y=="-":
    print(X-Z)
elif y=="*":
   print(X*Z)
elif y=="/":
   print(X/Z)
    
    

