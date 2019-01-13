# *args and **kwargs
def new_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"I would like to have {args[0]} {kwargs['fruit']}")

new_func(10,20,fruit='grapes',food='paneer',animal='dog')
