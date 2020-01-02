p=input("enter filename")
d=p.split(".")
if(d[-1]=='txt'):
    print("file is textfile")
elif(d[-1]=='py'):
    print("file is python file")
elif(d[-1]=='cpp'):
    print("file is c++ file")
else:
    print("file is c file")
