class CallCounter:
    def __init__(self):
        self.count = 0

    def __call__(self, increment=1):
        self.count += increment
        return f"Total calls: {self.count}"

# Instantiate the class
counter_instance = CallCounter()

# Call the instance directly like a function
print(counter_instance())   # Output: Total calls: 1
print(counter_instance(5))  # Output: Total calls: 6
print(counter_instance())   # Output: Total calls: 7