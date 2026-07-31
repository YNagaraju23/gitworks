class Test:
    def __enter__(self):
        return "resource data"
    def __exit__(self, exc_type, exc, tb):
        pass
with Test() as a:
    print("the resource point is ", a)