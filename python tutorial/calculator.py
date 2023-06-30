
#simple calculator
# num1 = int(input("Enter first number: "))
# symbol=input("Enter operator to perform :")
# num2=int(input("Enter second number: "))

# if symbol == "+":
#     print(num1+num2)
# elif symbol == "-":
#     print(num1-num2)
# elif symbol == "%":
#     print(num1%num2)
# elif symbol == "/":
#     print(num1/num2)
# elif symbol == "//":
#     print(num1//num2)
# else:
#     print("Invalid")


#print the calender
import calendar

yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))