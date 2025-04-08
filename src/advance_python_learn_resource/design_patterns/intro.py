# creational design patterns

import copy


class Singleton:
    """
    Ensures that only one instance of the class exists.

    This is achieved by making the constructor private and providing a static
    method to access the single instance. The first time the static method is
    called, a new instance is created and stored. Subsequent calls return
    the same stored instance.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Initialization logic (optional)
            cls._instance._initialized = False
        return cls._instance

    def initialize(self, data):
        """Initializes the singleton instance with some data."""
        if not self._initialized:
            self.data = data
            self._initialized = True
        else:
            print("Singleton already initialized.")

    def get_data(self):
        """Returns the data stored in the singleton instance."""
        return self.data


class Shape:
    """An abstract base class for shapes."""

    def draw(self):
        raise NotImplementedError("Subclasses must implement the draw method")


class Circle(Shape):
    """Represents a circle."""

    def draw(self):
        return "Drawing a circle"


class Square(Shape):
    """Represents a square."""

    def draw(self):
        return "Drawing a square"


class ShapeFactory:
    """
    A factory class to create different shape objects.

    This class encapsulates the instantiation logic for concrete Shape subclasses,
    allowing the client code to request a shape without knowing the specific
    implementation details.
    """

    @staticmethod
    def create_shape(shape_type):
        """
        Creates and returns a Shape object based on the given type.

        Args:
            shape_type (str): The type of shape to create ('circle' or 'square').

        Returns:
            Shape: An instance of the requested shape type, or None if the type is invalid.
        """
        if shape_type.lower() == "circle":
            return Circle()
        elif shape_type.lower() == "square":
            return Square()
        else:
            print(f"Shape type '{shape_type}' not recognized.")
            return None


class GUIFactory:
    """
    An abstract factory for creating related GUI elements.

    This interface defines the methods for creating different types of GUI
    components (e.g., buttons, text boxes) without specifying their concrete
    classes. Concrete factory subclasses will implement these methods to
    produce families of related GUI elements (e.g., Windows GUI, Mac GUI).
    """

    def create_button(self):
        """Creates a button."""
        raise NotImplementedError("Subclasses must implement create_button")

    def create_textbox(self):
        """Creates a text box."""
        raise NotImplementedError("Subclasses must implement create_textbox")


class WindowsGUIFactory(GUIFactory):
    """A concrete factory for creating Windows GUI elements."""

    def create_button(self):
        """Creates a Windows button."""
        return WindowsButton()

    def create_textbox(self):
        """Creates a Windows text box."""
        return WindowsTextBox()


class MacGUIFactory(GUIFactory):
    """A concrete factory for creating Mac GUI elements."""

    def create_button(self):
        """Creates a Mac button."""
        return MacButton()

    def create_textbox(self):
        """Creates a Mac text box."""
        return MacTextBox()


class Button:
    """Abstract base class for buttons."""

    def render(self):
        raise NotImplementedError("Subclasses must implement render")


class TextBox:
    """Abstract base class for text boxes."""

    def display(self):
        raise NotImplementedError("Subclasses must implement display")


class WindowsButton(Button):
    """A concrete Windows button."""

    def render(self):
        return "Rendering a Windows button"


class MacButton(Button):
    """A concrete Mac button."""

    def render(self):
        return "Rendering a Mac button"


class WindowsTextBox(TextBox):
    """A concrete Windows text box."""

    def display(self):
        return "Displaying a Windows text box"


class MacTextBox(TextBox):
    """A concrete Mac text box."""

    def display(self):
        return "Displaying a Mac text box"


def create_ui(factory: GUIFactory):
    """
    Creates and renders UI elements using the provided GUI factory.

    Args:
        factory (GUIFactory): The abstract factory to use for creating UI elements.
    """
    button = factory.create_button()
    textbox = factory.create_textbox()
    print(button.render())
    print(textbox.display())


class Pizza:
    """Represents a pizza with various attributes."""

    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = []
        self.toppings = []

    def __str__(self):
        return (
            f"Dough: {self.dough}\n"
            f"Sauce: {self.sauce}\n"
            f"Cheese: {', '.join(self.cheese)}\n"
            f"Toppings: {', '.join(self.toppings)}"
        )


class PizzaBuilder:
    """
    An abstract builder for constructing Pizza objects step by step.

    Concrete builder subclasses will define the specific steps for creating
    different types of pizzas. This allows for a consistent construction
    process with varying final representations.
    """

    def __init__(self):
        self.pizza = Pizza()

    def add_dough(self, dough):
        """Adds the type of dough to the pizza."""
        self.pizza.dough = dough
        return self

    def add_sauce(self, sauce):
        """Adds the type of sauce to the pizza."""
        self.pizza.sauce = sauce
        return self

    def add_cheese(self, cheese):
        """Adds a type of cheese to the pizza."""
        self.pizza.cheese.append(cheese)
        return self

    def add_topping(self, topping):
        """Adds a topping to the pizza."""
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        """Returns the constructed Pizza object."""
        return self.pizza


class VeggiePizzaBuilder(PizzaBuilder):
    """A concrete builder for creating veggie pizzas."""

    def __init__(self):
        super().__init__()
        self.add_dough("Thin crust")
        self.add_sauce("Marinara")
        self.add_cheese(["Mozzarella"])

    def add_veggies(self, veggies):
        """Adds a list of vegetables as toppings."""
        self.pizza.toppings.extend(veggies)
        return self


class MeatLoversPizzaBuilder(PizzaBuilder):
    """A concrete builder for creating meat lovers pizzas."""

    def __init__(self):
        super().__init__()
        self.add_dough("Thick crust")
        self.add_sauce("Tomato")
        self.add_cheese(["Mozzarella", "Cheddar"])

    def add_meats(self, meats):
        """Adds a list of meats as toppings."""
        self.pizza.toppings.extend(meats)
        return self


class Prototype:
    """
    An abstract prototype class declaring the clone operation.

    Concrete prototype classes will implement the `clone` method to create
    a copy of themselves. This allows for creating new objects by copying
    existing ones, potentially with modifications, without needing to know
    the specific class of the object being created.
    """

    def clone(self):
        """Returns a shallow copy of the prototype."""
        return copy.copy(self)


class ConcretePrototype1(Prototype):
    """A concrete prototype class."""

    def __init__(self, data):
        self.data = data

    def operation(self):
        return f"ConcretePrototype1 with data: {self.data}"


class ConcretePrototype2(Prototype):
    """Another concrete prototype class."""

    def __init__(self, value):
        self.value = value

    def process(self):
        return f"ConcretePrototype2 processing value: {self.value}"
