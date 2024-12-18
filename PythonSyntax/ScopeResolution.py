# variable scope = where q variable is visible anf accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Scope local variable
# def func1():
#     x = 3
#     print(x)
    
# def func2():
#     y = 2
#     print(y)
    
# func1()
# func2()

# Scope enclosed variable
# def func1():
#     x = 1
#     def func2():
#         nonlocal x
#         x = 2
#         print(x)
#     func2()
    
# func1()

# Scope global variable
# def func1():
#     print(x)
    
# def func2():
#     print(x)
    
# x = 3

# func1()
# func2()

from math import e

def func1():
    print(e)
    
func1()
