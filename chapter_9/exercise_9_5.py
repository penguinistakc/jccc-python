class Worker:
    def __init__(self, name, salary, years_worked):
        """
        Initialize a Worker object with name, salary, and years worked.
        """
        self._name = name
        self._salary = salary
        self._years_worked = years_worked

    def pension(self):
        """
        Calculate pension for a Worker: years worked * 10% of salary.
        """
        return self._years_worked * (0.10 * self._salary)

    def getname(self):
        """
        Return the name of the Worker.
        """
        return self._name

    def __str__(self):
        return f"Worker(Name: {self._name}, Salary: {self._salary}, Years Worked: {self._years_worked}, Pension: {self.pension():.2f})"


class Manager(Worker):
    def pension(self):
        """
        Calculate pension for a Manager: years worked * 20% of salary.
        """
        return self._years_worked * (0.20 * self._salary)

    def __str__(self):
        return f"Manager(Name: {self._name}, Salary: {self._salary}, Years Worked: {self._years_worked}, Pension: {self.pension():.2f})"


class Executive(Manager):
    def pension(self):
        """
        Calculate pension for an Executive: years worked * 30% of salary.
        """
        return self._years_worked * (0.30 * self._salary)

    def __str__(self):
        return f"Executive(Name: {self._name}, Salary: {self._salary}, Years Worked: {self._years_worked}, Pension: {self.pension():.2f})"


# Testing the classes
if __name__ == "__main__":
    # Create Worker, Manager, and Executive objects
    worker = Worker("Alice", 50000, 10)
    manager = Manager("Bob", 80000, 15)
    executive = Executive("Charlie", 120000, 20)

    # Print each object's details
    print(worker)
    print(manager)
    print(executive)

    # Use the getname() method for all classes
    print(f"Worker's name: {worker.getname()}")
    print(f"Manager's name: {manager.getname()}")
    print(f"Executive's name: {executive.getname()}")
