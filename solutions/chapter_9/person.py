class Person:
    def __init__(self, name, age, gender):
        """
        Initialize a Person object with name, age, and gender.
        """
        self._name = name
        self._age = age
        self._gender = gender

    # Getter and Setter for Name
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for Age
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # Getter and Setter for Gender
    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    # String Representation
    def __str__(self):
        return f"Person(Name: {self._name}, Age: {self._age}, Gender: {self._gender})"
