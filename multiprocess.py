from multiprocessing import Pool
def do_square(a):
    return a*a
if __name__ == "__main__":
    lst=[1,2,3,4,5]
    with Pool(processes=2) as pool:
        result=pool.map(do_square,lst)
    print(result)


#from multiprocessing import Pool
#
#def square(number):
#    return number * number
#
#if __name__ == "__main__":
#    numbers = [1, 2, 3, 4, 5]
#    # Creates a pool of 4 worker processes
#    with Pool(processes=4) as pool:
#        results = pool.map(square, numbers)
#    print(results)  # Output: [1, 4, 9, 16, 25]