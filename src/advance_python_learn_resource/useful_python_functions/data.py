ugly_dict = {
    "very_long_key_that_makes_reading_difficult": {
        "nested": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "deeply": {
            "nested": {
                "items": {"with": {"too": {"many": {"levels": [{"of": "nesting"}]}}}}
            }
        },
    },
    "inconsistent_spacing": {"some_values": [1, 2, 3], "other_values": [4, 5, 6]},
    "mixed_types": [1, "string", True, None, 3.14159, (1, 2, 3), {1: "one", 2: "two"}],
    "empty": {},
    "single_item": {"only_one": 1},
    "a": 1,
    "b": {
        "c": {
            "d": {
                "e": {
                    "f": {
                        "g": {
                            "h": {"i": {"j": {"k": {"l": {"m": {"n": {"o": "deep"}}}}}}}
                        }
                    }
                }
            }
        }
    },
}
