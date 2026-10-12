sub1 =int(input("Enter marks of maths:"))
sub2 =int(input("Enter marks of physics:"))
sub3 =int(input("Enter marks of chem:"))
sub4 =int(input("Enter marks of bio:"))
sub5 =int(input("Enter marks of history:"))

per=sub1+sub2+sub3+sub4+sub5/500*100

if(per>45):
 if(per>90):
    print("Grade:A")
 elif(per>80 and per<90):
    print("Grade:B")
 elif(per>70 and per<80):
    print("Grade:C")
 else:
     print("Grade:D")
else:
    print("Sorry :( You are fail")
    
avg = (sub1+sub2+sub3+sub4+sub5)/5
print("Your Average marks is:",avg)
    



