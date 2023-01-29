#make a calculator
print("first number daal ree... ")
a=float(input())

print("select a operator")
x=input()

print ("second number enter kr ree... ")
b=float(input())

if x=="+":
 print(a+b)
elif x=="-":
 print(a-b)
elif x=="/":
 print(a/b)
elif x=="*":
 print(a*b)
else:
 print("invalid input ree...")
