

print('''
      'CALCULATOR'
      1.ADDITION
      2.SUBTRACTION
      3.MULTIPLICATION
      4.DIVISION''')

def add(x,y):

    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return  x * y

def division(x,y):
    if y== 0:
        print(ValueError)
        return x/y
    while True:()

Choice = int(input("Enter Your Choice [1,2,3,4] : "))

if Choice in [1,2,3,4]:

 sum1 = int(input("Enter Your First Number : "))
 sum2 = int(input("Enter Your Second Number : "))


if Choice == 1 :
             result = add(sum1,sum2)
             print("Result",result)



elif Choice == 2:
              result1= subtract(sum1, sum2)
              print("Result", result1)

elif Choice ==  3:
              result2= multiply(sum1, sum2)
              print("Result", result2)

elif Choice == 4:
              result3= division(sum1,sum2)
              print("result",  result3)


else:
        print("Error")