from person import Person

"""Create a class called Person.
Each Person should have a name, an age, and a gender.
In addition to getters and setters for the above methods, the
Person class should have a __init__ method and a
__str__ method.
Therefore, the following application should test your work.
p1 = Person("Michael", 45, "M")
print(p1)"""

# Test the Person class
if __name__ == "__main__":
    p1 = Person("Michael", 45, "M")
    print(p1)
