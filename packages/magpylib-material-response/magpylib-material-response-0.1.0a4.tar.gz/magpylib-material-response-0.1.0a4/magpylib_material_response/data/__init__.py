"""
Built-in datasets for demonstration, educational and test purposes.
"""


def get_dataset(name):
    import json
    import os

    file = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "package_data",
        "datasets",
        name,
    )
    with open(file) as fp:
        sim = json.load(fp)
    return sim
