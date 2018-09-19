def cartesian(iterable):
    """
    Given the iterable of length n::

        [0, 1, 2, ..., n-1, n]

    yields each item paired with every other item (sorted)::

        [
            (0, 1),
            (0, 2),
            ...
            (0, n),
            (1, 2),
            ...
            (n-1, n)
        ]

    """
    static = list(iterable)
    for i, prim in enumerate(static):
        for sec in static[i + 1 :]:
            yield (prim, sec)


def key_from(iterable):
    """Returns a sorted hashable key from an iterable"""
    return "/".join(sorted(iterable))


class Cooccurrence:
    def __init__(self, lines):
        """
        Parse and set data on `lookup`, where this is a dict like::

            {
              "ALICE/BOB": 1,
              ...
            }
        
        """
        self.lookup = {}

        for line in lines:
            tokens = line.rstrip().split(" ")
            for pair in cartesian(tokens):
                k = key_from(pair)
                count = self.lookup.get(k, 0)
                self.lookup[k] = count + 1

    def get(self, *tokens):
        """
        Retrieve the number of lines that contain all n tokens
        """
        return self.lookup.get(key_from(tokens), 0)

