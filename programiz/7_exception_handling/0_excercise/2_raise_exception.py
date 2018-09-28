def enter_age(age):
    if age < 0:
        raise ValueError("Only positive integers allowed")
    if age % 2 == 0:
        print "Age is even"
    else:
        print "Age is odd"

try:
    num = int(raw_input("Enter your age: "))
    enter_age(num)

except ValueError:
    print "Only positive integers are allowed."
except:
    print "Something is wrong"
