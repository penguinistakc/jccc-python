from family_ex_9_4 import Family
from family_error import FamilyError
from person import Person

"""Implement the necessary special methods so that the <,
==, and > operators can be used with Family objects.
The criteria for the methods should be the number of children in
each Family.
myFamily = Family(mom, dad, kid1, kid2)
smiths = Family(mom, dad, kid1)
if (myFamily > smiths):
print("we have more kids than smiths")
if (myFamily == smiths):
print("families have same # of kids")
if (myFamily < smiths):
print("we have fewer kids than smiths")"""

# Test the classes
if __name__ == "__main__":
    try:
        # Create parent and child objects
        mom = Person("Mommy", 45, "F")
        dad = Person("Daddie", 45, "M")
        kid1 = Person("Johnie", 2, "M")
        kid2 = Person("Janie", 3, "F")

        # Create two Family objects
        myFamily = Family(mom, dad, kid1, kid2)  # 2 children
        smiths = Family(mom, dad, kid1)  # 1 child

        # Comparison testing
        if myFamily > smiths:
            print("We have more kids than the Smiths.")
        if myFamily == smiths:
            print("Families have the same number of kids.")
        if myFamily < smiths:
            print("We have fewer kids than the Smiths.")

        # Add another child to the Smiths
        smiths.add(kid2)

        if myFamily == smiths:
            print("Now the families have the same number of kids.")

    except FamilyError as fe:
        print(f"FamilyError: {fe}")
