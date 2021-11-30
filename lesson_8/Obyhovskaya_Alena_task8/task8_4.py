
def val_checker(input_arg):
    def the_real_decorator(func):
        def wrapper(arg):
            if not input_arg(arg):
                raise ValueError(f'wrong value: {arg}')
            else:
                print(func(arg))
        return wrapper

    return the_real_decorator

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

calc_cube(7)
