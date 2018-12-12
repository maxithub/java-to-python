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


# No ( ) for condition checking, e.g. if, while
if 1 == 2:
    print("Never happen")
else:
    print("Always true")

i = 0
while i < 10:
    print(str(i))
    i += 1

# No need to specify type when declare variable
integer = 1
string = "Hello"


# Use def keyword to define method
def do_something():
    print("Doing something...")


# exception handling
try:
    error_list = [0, 1, 2, 3, 4]
    print(error_list[4])

    if 1 == 1:
        raise ValueError("Oops")

except IndexError as e:
    print(f"Index error {e.args}")
except (IOError, ValueError):
    print("Something wrong with IO or Value")
else:
    print("Unknown error")
finally:
    print("Do some clean up here")


# Use global keyword to access global variables
global_counter = 100


def increase():
    global global_counter
    global_counter += 1


# empty block
def empty_function():
    pass


# no method overloading, use default argument, *args and **kwars
def default_arg(a, b, c="c", d="d"):
    print(f"{a}, {b}, {c}, {d}")


default_arg("a", "b", "d")
default_arg("1", "2")
default_arg("1", "2", d="3")


def var_args(a, b, *args):
    print(f"{a}, {b}, {args}")


var_args("a", "b", "c")
var_args("a", "b", "c", "d", "e")
var_args("a", "b", "c", 1, 2)


def print_table(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_table(a=5, b=6, c=7)

# ------------------------- Big syntax differences ----------------------------
# ------- bool (Java boolean) -------
# is vs ==
str1 = "hello"
str2 = "hello"
print(str1 == str2)
print(str1 is str2)

print(bool(None))
print(bool("abc"))
print(bool(12))
print(bool(0))
print(bool([]))
print(bool([1]))

print(True and False)
print(True & False)


# ------- string -------
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
# print(dir(str))
# print(help(str))


# ------- numeric types: int, float and complex -------
an_integer = 1234
an_float = 1234.56
an_complex = 2 - 1j
print(an_complex)

# convert string to number
integer_from_str = int("12345")
print(integer_from_str)
float_from_str = float("123456.689")
print(float_from_str)

# new operator
power_op = 2 ** 3
print(power_op)
floor_division = 3 // 2
print(floor_division)


# ------- list -------
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list)
print(my_list[0])
print(my_list[-1])
print(my_list[1:3])
print(my_list[1: -2])
print(my_list[-3:])
print(len(my_list))

my_list.append(7)
print(my_list)
my_list.extend([8, 9, 10])
print(my_list)

combined_list = my_list + [11, 12]
print(combined_list)

del my_list[7]
print(my_list)
del my_list[2:4]
print(my_list)

my_list.sort(reverse=True)
print(my_list)
new_sorted_list = sorted(my_list)
print(new_sorted_list)

print(4 in my_list)
print(19 in my_list)

for n in my_list:
    print(n)

for i, n in enumerate(my_list, start=2):
    print(f"my_list[{i}]={n}")

# ------- tuple, as immutable list -------
an_tuple = (0, 1, 2, 3)
print(an_tuple)


def multiple_return():
    return 1, "two", 3


print(multiple_return())


# ------- set -------
an_set = {0, 1, 2, 3, 4}
print(an_set)

# ------- empty list, tuple, set -------
empty_list_1 = []
empty_list_2 = list()

empty_tupble_1 = ()
empty_tupble_2 = tuple()

# empty_set = {} # Not right, this is dict
empty_set = set()

# ------- list map, filter vs comprehension -------
my_list_2 = list(map(lambda k: k * 2, my_list))
print(my_list_2)
my_list_3 = [k * 2 for k in my_list]
print(my_list_3)

my_list_4 = list(filter(lambda k: k % 2 == 0, my_list))
print(my_list_4)
my_list_5 = [k for k in my_list if k % 2 == 0]
print(my_list_5)

# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# ------- dict (map in Java) -------

a_dict = {"one": 1, "two": 2, "three": 3}
print(a_dict)
print(a_dict["two"]) # this will throw error if the key doesn't exist
print(a_dict.get("three"))

a_dict.update({"one": 11, "four": 4})
print(a_dict)

del a_dict["one"]
print(a_dict)

for (k, v) in a_dict.items():
    print(f"{k}={v}")


# define class

# Everything is an object

class Account(object):
    # static field
    counter = 0

    # Constructor
    def __init__(self, id, balance):
        Account.counter += 1
        self.id = id
        self.balance = balance

    # toString() in Java
    def __str__(self):
        return f"id = {self.id}, balance = {self.balance}, counter = {Account.counter}"

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


from_account = Account(1, 100)
to_account = Account(2, 50)
print(from_account)
print(to_account)
Account.transfer(from_account, to_account, 30)
print(from_account)
print(to_account)

# abstract class (no interface)
from abc import ABC, abstractmethod


class MyAbc1(ABC):
    @abstractmethod
    def my_abc1(self):
        pass


class MyAbc2(ABC):
    @abstractmethod
    def my_abc2(self):
        pass


class MyClass(MyAbc1, MyAbc2):
    def my_abc1(self):
        print("my_abc1 is called")

    def my_abc2(self):
        print("my_abc2 is called")


# my_abc1 = MyAbc1()

my_class = MyClass()
my_class.my_abc1()
