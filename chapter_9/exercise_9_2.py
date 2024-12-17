class Person:
    def __init__(self, name, age, gender):
        """
        Initialize a Person object with name, age, and gender.
        """
        self._name = name
        self._age = age
        self._gender = gender

    # Getters and Setters
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    # String Representation
    def __str__(self):
        return f"{self._name}, Age: {self._age}, Gender: {self._gender}"


class Family:
    def __init__(self, parent1, parent2, *children):
        """
        Initialize a Family object with two parents and optional children.
        """
        if not isinstance(parent1, Person) or not isinstance(parent2, Person):
            raise ValueError(
                "The first two arguments must be Person objects (parents)."
            )

        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        """
        Add a child to the family.
        """
        if not isinstance(child, Person):
            raise ValueError("The child must be a Person object.")
        self.children.append(child)

    def __str__(self):
        """
        String representation of the Family object.
        """
        family_str = f"Parents:\n  {self.parent1}\n  {self.parent2}\n"
        if self.children:
            family_str += "Children:\n"
            for child in self.children:
                family_str += f"  {child}\n"
        else:
            family_str += "No children in this family.\n"
        return family_str.strip()


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
