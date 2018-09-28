def division(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print "a/b result in 0"
    else:
        print c

division(4, 7)
division(1, 1)
