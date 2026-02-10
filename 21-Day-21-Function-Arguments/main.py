# Default arguments:
# def name(fname, mname = "jhon", lname = "Watson"):
#     print("Hello, ",fname, mname, lname)
# name("Amy")

# Keyword arguments
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name(mname = "Peter", lname = "Wesker", fname = "Jade")

# Required arguments
# 1)when no of arguments passed does not match to the actual function definition.
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Quill")
# 2)when no of arguments passed matches to the actual function definition
# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)
# name("Peter", "Ego", "Quill")

# variable-length arguments:
# arbitary arguments

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
        # print("Average is: ", sum / len(numbers))
        # return 7
    return sum / len(numbers)

average(4, 6)
# average(b=9)


