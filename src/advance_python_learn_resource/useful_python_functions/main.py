import pprint
from collections import defaultdict


def print_data(data: dict):
    """
    Print the data in a pretty format.
    """
    pprint.pprint(data)


def default_dict_check():
    # Assigns val_1 to a default dict with int as the default factory
    val_1 = defaultdict(int)
    print(type(val_1))
    print(val_1)

    # TODO: what can i use it for


if __name__ == "__main__":
    # print_data(ugly_dict)
    default_dict_check()
