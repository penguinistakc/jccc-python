class Family:
    def __init__(self, parent1, parent2, *children):
        """
        Initialize a Family object with two parents and optional children.
        """
        self.parent1 = parent1
        self.parent2 = parent2
        self.children = list(children)

    def add(self, child):
        """
        Add a child to the family.
        """
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
