
# #один аргумент
def type_logger(func):
    def wrapper_type_arguments(arg):
        print('Один аргумент: ')
        print(f'{arg} : {type(arg)}')
        print(f'результат вычисления :{func(arg)}\n')
    return wrapper_type_arguments

@type_logger
def calc_cube(x):
    return x ** 3

calc_cube(10)

# два аргумент c выводом имени функции и типом результата вычиесления
def type_logger(func):
    def wrapper_type_arguments(x,y):
        print('Два аргумента: ')
        print(f'{func.__name__}({x} : {type(x)} , {y} : {type(y)})')
        a = func(x,y)
        print(f'Резульат вычисления: {a},{type(a)}\n')
    return wrapper_type_arguments

@type_logger
def calc_cube_keyarg(x, y):
    return x + y

calc_cube_keyarg(10,5.5 )


# именованные аргументы

def type_logger(func):
    def wrapper_type_arguments(x,y):
        print('Именованые аргументы: ')
        print(f'{func.__name__}({x} : {type(x)} , {y} : {type(y)})')
        a = func(x,y)
        print(f'Резульат вычисления: {a},{type(a)}\n')
    return wrapper_type_arguments

@type_logger
def calc_cube_keyarg(x, y):
    return x - y

calc_cube_keyarg(y = 50, x = 10)

# переменное число аргументов
def type_logger(func):
    def wrapper_type_arguments(*arg):
        for ar in arg:
            print(f'{ar} : {type(ar)},')
        print(f'Резульат вычисления всех аругментов (возведение в куб):{func(*arg)}')
    return wrapper_type_arguments

@type_logger
def calc_cube(*x):
    res = [i ** 3 for i in x]
    return res

calc_cube(5, 6, 14.5)