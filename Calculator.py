print("This is the first Task of the internship")
print("This Whole Program is to Make a calculator with different operations!!")

def calc():
    n=int(input("Enter the first operand:"))
    m=int(input("Enter the Second Operand:"))
    print(''' \t    1: + (Addition)
            2: - (Substraction)
            3: * (Multiply)
            4: / (Divide)
            5: % (Modulus)''')
    opr=input("Enter any of the operator from the Above given operators")
    if opr=="+":
        sum = n+m
        print("Addition of the two given numbers is:",sum)
    elif opr=="-":
        if n>m:
            diff=n-m
            print(n,"is greater than",m)
            print("Substraction",n,"-",m,"=",diff)
        else:
            dif=m-n
            print(m,"is greater than",n)
            print("Substraction",m,"-",n,"=",dif)
    elif opr=="*":
            mul=n*m
            print("Multiplication Result",n,"*",m,"=",mul)

    elif opr=="/":  
         try:
             div=n/m
             print("Division of n and m is",div)
         except:
            print("Exception occured:-Division by zero!!")
            print("You need to restart the calculator for again division")
            print("CALCULATOR RESTARTED")
            calc()
    elif opr=="%":
            modu=n%m
            print("Modulus of n and m is",modu)
    else:
          print("Please Enter a valid Operator from the above")
calc()


def exitfn():
 ext=input("Do you Want to exit (YES or NO)")
 if ext=="YES":
  print("EXIT SUCESSFULLY")
 elif ext=="NO":
   print("CALCULATOR RESTARTED")
   calc()
 else:
     print("You have entered the wrong Word Plz Enter YES or NO")
     exitfn()
exitfn()