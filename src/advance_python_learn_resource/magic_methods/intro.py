# magic_methods.py

"""
When a new class is created without explicit magic method definitions,
it inherits default implementations from the base 'object' class. These
defaults provide fundamental object behavior or raise TypeError for
operations requiring custom logic.

Implicitly available magic methods with default behavior include:

- __new__(cls, *args, **kwargs): Instance creation.
- __init__(self): Instance initialization (no action by default).
- __repr__(self): String representation (class name and memory address).
- __str__(self): User-friendly string (defaults to __repr__).
- __bytes__(self): Byte representation (raises TypeError).
- __hash__(self): Hash value (if object is hashable by default).
- __bool__(self): Boolean evaluation (True unless __len__ is zero).
- Comparison methods (__lt__, __le__, __eq__, __ne__, __gt__, __ge__):
  Compare based on object identity.
- Attribute access methods (__getattr__, __setattr__, __delattr__):
  Handle attribute access, assignment, and deletion.
- Container methods (__len__, __getitem__, __setitem__, __delitem__,
  __iter__, __contains__): Typically raise TypeError if called, requiring
  custom implementation for container-like behavior.

Customizing these methods is necessary to deviate from the default
behavior and implement specific functionality for class instances.
"""


class Person:
    """Represents a person with a name and age."""

    def __init__(self, name, age):
        """Initializes a new Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age


class Car:
    """Represents a car with a make and model."""

    def __init__(self, make, model):
        """Initializes a new Car object.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
        """
        self.make = make
        self.model = model

    def __str__(self):
        """Returns a user-friendly string representation of the Car object."""
        return f"{self.make} {self.model}"


class Point:
    """Represents a point in 2D space."""

    def __init__(self, x, y):
        """Initializes a new Point object.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """Returns a string representation of the Point object that could be used to recreate it."""
        return f"Point({self.x}, {self.y})"


class CustomList:
    """A custom list-like object."""

    def __init__(self, items):
        """Initializes a new CustomList object.

        Args:
            items (list): A list of items to be stored in the CustomList.
        """
        self.items = items

    def __len__(self):
        """Returns the number of items in the CustomList."""
        return len(self.items)


class MyList:
    """A custom list that allows item access using indexing."""

    def __init__(self, data):
        """Initializes a new MyList object.

        Args:
            data (list): The initial list of data.
        """
        self.data = data

    def __getitem__(self, index):
        """Retrieves an item from the MyList at the given index.

        Args:
            index (int): The index of the item to retrieve.

        Returns:
            The item at the specified index.
        """
        return self.data[index]


class MyDict:
    """A custom dictionary-like object that allows item assignment using keys."""

    def __init__(self, data=None):
        """Initializes a new MyDict object.

        Args:
            data (dict, optional): The initial dictionary data. Defaults to None (empty dictionary).
        """
        self.data = data if data is not None else {}

    def __setitem__(self, key, value):
        """Sets the value of an item in the MyDict with the given key.

        Args:
            key: The key of the item to set.
            value: The value to assign to the key.
        """
        self.data[key] = value


class MyListDeletable:
    """A custom list that allows item deletion using indexing."""

    def __init__(self, data):
        """Initializes a new MyListDeletable object.

        Args:
            data (list): The initial list of data.
        """
        self.data = data

    def __delitem__(self, index):
        """Deletes the item at the specified index from the MyListDeletable.

        Args:
            index (int): The index of the item to delete.
        """
        del self.data[index]


class Squares:
    """An iterator that generates the squares of numbers up to a given length."""

    def __init__(self, length):
        """Initializes a new Squares iterator.

        Args:
            length (int): The number of squares to generate.
        """
        self.length = length
        self.current = 0

    def __iter__(self):
        """Returns the iterator object itself."""
        return self

    def __next__(self):
        """Returns the next square in the sequence.

        Raises:
            StopIteration: If all squares have been generated.

        Returns:
            int: The next square.
        """
        if self.current >= self.length:
            raise StopIteration
        result = self.current**2
        self.current += 1
        return result


class MyContainer:
    """A custom container that allows checking if an item is present."""

    def __init__(self, items):
        """Initializes a new MyContainer object.

        Args:
            items (list): The list of items in the container.
        """
        self.items = items

    def __contains__(self, item):
        """Checks if the given item is present in the container.

        Args:
            item: The item to check for.

        Returns:
            bool: True if the item is in the container, False otherwise.
        """
        return item in self.items


class Multiplier:
    """A callable object that multiplies a number by a fixed factor."""

    def __init__(self, factor):
        """Initializes a new Multiplier object.

        Args:
            factor (int): The factor to multiply by.
        """
        self.factor = factor

    def __call__(self, num):
        """Multiplies the given number by the internal factor.

        Args:
            num (int): The number to multiply.

        Returns:
            int: The result of the multiplication.
        """
        return num * self.factor


# Examples

print("\n--- __init__ Example ---")
person1 = Person("Alice", 30)
print(f"Person name: {person1.name}, age: {person1.age}")

print("\n--- __str__ Example ---")
car1 = Car("Toyota", "Corolla")
print(car1)

print("\n--- __repr__ Example ---")
point = Point(3, 4)
print(repr(point))

print("\n--- __len__ Example ---")
clist = CustomList([1, 2, 3, 4, 5])
print(f"Length of custom list: {len(clist)}")

print("\n--- __getitem__ Example ---")
my_list = MyList([10, 20, 30])
print(f"Element at index 1: {my_list[1]}")

print("\n--- __setitem__ Example ---")
my_dict = MyDict()
my_dict["name"] = "Bob"
print(f"MyDict after setting item: {my_dict.data}")

print("\n--- __delitem__ Example ---")
my_list_deletable = MyListDeletable([1, 2, 3])
del my_list_deletable[1]
print(f"MyListDeletable after deletion: {my_list_deletable.data}")

print("\n--- __iter__ and __next__ Example ---")
squares = Squares(3)
print("Squares:")
for square in squares:
    print(square)

print("\n--- __contains__ Example ---")
container = MyContainer([1, 2, 3])
print(f"Is 2 in the container? {2 in container}")
print(f"Is 4 in the container? {4 in container}")

print("\n--- __call__ Example ---")
double = Multiplier(2)
print(f"2 multiplied by 5: {double(5)}")
