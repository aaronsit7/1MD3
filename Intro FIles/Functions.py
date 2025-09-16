"""
myJavaVariable = 9
def my_function(x, y):
    return x + y

print(my_function(9, 1))

a = my_function(4, 4)
print(a)

tax_rate = 0.17

def calc_tax(income):
    return tax_rate * income

def get_income(tax):
    return tax/tax_rate

def get_amount_owed(tax_paid, income):
    return calc_tax(income) - tax_paid

def f1(x):
    print(x)
    print(x)
    return

def f2(x):
    print(x)
    print(x)
    return x

def f3(x):
    return x
    print(x)
    print(x)

def f4(x):
    print(x)
    return x
    print(x)
    return x

def pizzas_to_order(adults, children):
    total_slices = 3*adults + children
    return total_slices//8 + min(1, total_slices%8)

x = 5

def my_fun(y):
    return y + x

print(my_fun(6))
"""

y = 5
def my_fun(y):
    y = y+1
    return y