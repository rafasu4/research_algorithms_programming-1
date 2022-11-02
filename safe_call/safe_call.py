

def kwargs_handler(func, **kwargs) -> dict:
    kwargs_dic = dict()
    # holding all of the given arguments and their type
    for key, arg in kwargs.items():
            kwargs_dic[key] = type(arg)
    dic = func.__annotations__  # holding the given func's argument annotation
    for key, value in kwargs_dic.items():
        if key in dic:
            if value != dic[key]:
                raise Exception('Wrong type parameters were entered!')

def args_handler(func, *args) -> tuple:
    args_tup = tuple()
    annot_tup = tuple()
    for v in func.__annotations__.values():
        if len(annot_tup) == len(args):
            break
        annot_tup += (v,)
    for arg in args:
        if(len(args_tup) == len(annot_tup)):
            break
        args_tup += (type(arg),)
    if args_tup != annot_tup:
        raise Exception('Wrong type parameters were entered!')

def safe_call(func, *args, **kwargs):
    if len(kwargs) != 0 and len(args) != 0:
        kwargs_handler(func, **kwargs)
        args_handler(func, *args)
        return func(*args, **kwargs)
    elif len(kwargs) != 0:
        kwargs_handler(func, **kwargs)
        return func(**kwargs)
    elif len(args) != 0:
        args_handler(func, *args)
        return func(*args)

def stam_func(x:int , y:float, z):
    return x+y+z


if __name__ == "__main__":
    print(safe_call(stam_func, 3, y=7.0, z=3))
