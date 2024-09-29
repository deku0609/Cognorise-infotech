num1= float(input("enter first number: "))
num2= float(input("enter second number: "))
op= input("select the type of operation(+, -, *, /): ")
if op=='+' :
    print("solution= ", num1+num2)
elif op=='-':
    print("solution= ", num1-num2)
elif op=='*':
    print("solution= ", num1*num2)
elif op=='/':
    print("solution= ", num1/num2)
else:
    print("invalid input!")                
