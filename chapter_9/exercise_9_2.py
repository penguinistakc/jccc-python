from person import Person
from family_ex_9_2 import Family

"""Create a class called Family.
The Family should be composed of two Person objects
representing the parents and a list of Person objects
representing the children.
• Therefore, the __init__ method should take two required
parameters, followed by a variable number of arguments.
• The first two Person objects will be the parents, and any
remaining objects will be children.
• Use the following to test your classes.
mom = Person("Mommy", 45, "F")
dad = Person("Daddie", 45, "M")
kid1 = Person("Johnie", 2, "M")
kid2 = Person("Janie", 3, "F")
myFamily = Family(mom, dad, kid1, kid2)
kid3 = Person("Paulie", 1, "M")
myFamily.add(kid3)
print(myFamily)
• Note the add method in the Family class.
"""

# Test the classes
if __name__ == "__main__":
    mom = Person("Mommy", 45, "F")
    dad = Person("Daddie", 45, "M")
    kid1 = Person("Johnie", 2, "M")
    kid2 = Person("Janie", 3, "F")

    # Create a Family object
    myFamily = Family(mom, dad, kid1, kid2)

    # Add another child
    kid3 = Person("Paulie", 1, "M")
    myFamily.add(kid3)

    # Print the Family
    print(myFamily)
