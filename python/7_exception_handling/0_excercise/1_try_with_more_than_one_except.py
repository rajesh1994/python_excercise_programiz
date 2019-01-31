# A try statement with more than one except statement.

try:
    num1, num2 = eval(raw_input("Enter two numbers, seperated by comma: "))
    result = num1 / num2
    print "Result is", result
    
except ZeroDivisionError:
    print "Division by zero is error!!"

except SyntaxError:
    print "Comma is missing. Enter numbers seperated by comma like this 1, 3"

except:
    print "Wrong Input"

else:
    print "No exceptions"

finally:
    print "This will execute no matter what"
