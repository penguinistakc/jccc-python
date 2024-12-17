from family_ex_9_2 import Family
from family_error import FamilyError
from person import Person

"""Create an exception class named FamilyError.
This exception should get raised when there is an attempt to
add a non-Person object to a Family object.
• Remember that Person objects can be added in both the
__init__ method and the add method.
"""


# Test the classes
if __name__ == "__main__":
    try:
        # Create parent and child objects
        mom = Person("Mommy", 45, "F")
        dad = Person("Daddie", 45, "M")
        kid1 = Person("Johnie", 2, "M")
        kid2 = Person("Janie", 3, "F")

        # Create a Family object
        myFamily = Family(mom, dad, kid1, kid2)

        # Add another child
        kid3 = Person("Paulie", 1, "M")
        myFamily.add(kid3)

        # Attempt to add an invalid child
        myFamily.add("NotAPerson")

        # Print the Family
        print(myFamily)
    except FamilyError as fe:
        print(f"FamilyError: {fe}")
