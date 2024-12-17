from employee import Worker, Manager, Executive

"""Implement the following class hierarchy.
Define a Worker class with a name, a salary, and number of
years worked.
• Provide a method named pension that returns an amount
equal to the years worked times 10% of the salary.
Derive Manager from Worker.
• A manager's pension is defined by the number of years
worked times 20% of the salary.
Derive Executive from Manager.
• An executive's pension is defined by the number of years
worked times 30% of the salary.
Implement a getname() method in the Worker class and have
this be a default method for all derived classes.
"""

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
