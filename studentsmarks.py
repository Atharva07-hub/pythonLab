num1 = int(input("Enter your number:"))
num2 = int(input("Enter secomd number:"))
print("select one operator:\n1.*\n2.+\n3.-\n 4./\n5.//\n6.%\n7.**")
opt = int(input(":"))
if(opt==1):
    print(num1*num2)
elif(opt==2):
    print(num1+num2)
elif(opt==3):
    print(num1-num2)
elif(opt==4):
    print(num1/num2)
elif(opt==5):
    print(num1//num2)
elif(opt==6):
    print(num1%num2)
else:
    print(num1**num2)    
    

