class FamilyError(Exception):
    """
    Custom exception for Family class errors.
    """

    def __init__(self, message):
        super().__init__(message)


class Person:
    def __init__(self, name, age, gender):
        """
        Initialize a Person object with name, age, and gender.
        """
        self._name = name
        self._age = age
        self._gender = gender

    def __str__(self):
        return f"{self._name}, Age: {self._age}, Gender: {self._gender}"


class Family:
    def __init__(self, parent1, parent2, *children):
        """
        Initialize a Family object with two parents and optional children.
        """
        if not isinstance(parent1, Person) or not isinstance(parent2, Person):
            raise FamilyError(
                "The first two arguments must be Person objects (parents)."
            )

        self.parent1 = parent1
        self.parent2 = parent2
        self.children = []

        # Validate and add children
        for child in children:
            if not isinstance(child, Person):
                raise FamilyError("All children must be Person objects.")
            self.children.append(child)

    def add(self, child):
        """
        Add a child to the family.
        """
        if not isinstance(child, Person):
            raise FamilyError("The child must be a Person object.")
        self.children.append(child)

    def __len__(self):
        """
        Return the number of children in the family.
        """
        return len(self.children)

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

    # Comparison methods based on the number of children
    def __lt__(self, other):
        if not isinstance(other, Family):
            return NotImplemented
        return len(self) < len(other)

    def __eq__(self, other):
        if not isinstance(other, Family):
            return NotImplemented
        return len(self) == len(other)

    def __gt__(self, other):
        if not isinstance(other, Family):
            return NotImplemented
        return len(self) > len(other)


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
