# ------------------------- Hello World ----------------------------
print("Hello, World")

# ------------------------- Big syntax differences ----------------------------

# No need ; for ending lines
message = "Hello World"


# No { }, use indentation and :
def say_hello(name):
    if name:
        print("Hello " + name)
    else:
        print("What is your name?")


# 03


# No need to specify type when declare variable
integer = 1
string = "Hello"


# use def keyword to define method
def do_something():
    print("Doing something...")


# 05 use global keyword to access global variables
global_counter = 100


def increase():
    global global_counter
    global_counter += 1


# define class
class Account(object):
    # Constructor
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance

    # toString() in Java
    def __str__(self):
        return "id = " + self.id + ", balance = " + self.balance

    # instance method
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    # static method
    @staticmethod
    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)

    @classmethod
    def from_dict(cls, a_dict):
        return cls(a_dict['id'], a_dict['balance'])


# Data types
## string
double_quote = "same as Java 'single quote' inside"
print(double_quote)
single_quote = 'single quote "double quote" inside'
print(single_quote)
multiple_lines = """
Line 1
Line 2
Line 3
"""
print(multiple_lines)

check_len = "hello"
print(len(check_len))

# substring
substring_digits = "0123456789"
print(substring_digits[0:3])
print(substring_digits[3:])
print(substring_digits[2:-1])
print(substring_digits[-3:])
print(substring_digits[:-3])
print(substring_digits[3])

# repeat
ha = "ha"
three_ha = ha * 3
print(three_ha)

# + still works as Java
part1 = "Hello"
part2 = "World"
whole_with_plus = part1 + " " + part2
print(whole_with_plus)

# need to explicitly cast to str
print("Python " + str(3))

# format
whole_with_format = "{} {}".format(part1, part2)
print(whole_with_format)
whole_with_f = f"{part1} {part2}" # Python 3.6+
print(whole_with_f)
whole_with_f2 = f"{part1} {part2.upper()}" # Python 3.6+
print(whole_with_f2)
whole_with_percentage = "%s %s" % (part1, part2)
print(whole_with_percentage)

# check methods
print(dir(str))
print(help(str))



# https://docs.python.org/3/tutorial/introduction.html#strings

# number
