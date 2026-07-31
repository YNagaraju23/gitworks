try:
    import math
except ImportError as error:
        raise RuntimeError("this is an import error")

age=35
if age>0:
    raise ValueError("age is under 35")