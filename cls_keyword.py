#cls is not actually a built-in keyword, but a conventional variable name used as the first argument in class methods to reference the class itself
class Employee:
    # Class-level variable shared by all instances
    company_name = "Tech Corp"

    @classmethod
    def change_company(cls, new_name):
        # Accesses and modifies the class variable via 'cls'
        cls.company_name = new_name