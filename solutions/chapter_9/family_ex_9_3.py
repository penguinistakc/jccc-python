from family_error import FamilyError
from person import Person


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
