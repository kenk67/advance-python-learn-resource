from dataclasses import dataclass, field

"""
Always use default_factory for mutable types like lists or dictionaries.
"""


@dataclass
class User:
    name: str
    hobbies: list[str] = field(default_factory=list)


if __name__ == "__main__":
    user_1 = User(name="John")
    user_2 = User(name="Jane")

    user_1.hobbies.append("Reading")
    user_2.hobbies.append("Writing")
    print("----This is the only way to use dataclass with default factory----")
    print(user_1)
    print(user_2)
