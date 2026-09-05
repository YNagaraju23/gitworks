#When a with statement executes, Python triggers these two special methods in a specific sequence:__enter__(self): Executes at the start of the with block. It sets up the resource and optionally returns an object assigned to the as variable.__exit__(self, exc_type, exc_val, exc_tb): Executes when leaving the with block, regardless of whether the code finished successfully or raised an error. It handles resource cleanup and exception management.

class ManagedResource:
    def __enter__(self):
        print("1. Entering: Setting up the resource.")
        # Open a file, connect to a database, or acquire a lock here
        return self  # This value is assigned to the variable after 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("3. Exiting: Cleaning up the resource.")
        # Close files, disconnect, or release locks here
        
        if exc_type:
            print(f"   An exception occurred: {exc_val}")
            # Return True to suppress the exception, or False to let it propagate
            return False 

# Using the context manager
with ManagedResource() as resource:
    print("2. Inside the 'with' block performing operations.")

    
class Test:
    def __enter__(self):
        return "resource data"
    def __exit__(self, exc_type, exc, tb):
        pass
with Test() as a:
    print("the resource point is ", a)