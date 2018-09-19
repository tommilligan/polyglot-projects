class Cooccurrence:
    def __init__(self, lines):
        """
        Parse and set data on `lookup`, where this is a dict like::

            {
              "ALICE": Set([0]),
              "BOB": Set([0, 1]),
              ...
            }
        
        """
        self.lookup = {}

        for i, line in enumerate(lines):
            tokens = line.rstrip().split(" ")
            for token in tokens:
                indexes = self.lookup.get(token, [])
                self.lookup[token] = indexes + [i]

        # dedupe indexes in each key here
        for k, v in self.lookup.items():
            self.lookup[k] = set(v)

    def get(self, *tokens):
        """
        Retrieve the number of lines that contain all n tokens
        """
        indexes = [self.lookup.get(token, set()) for token in tokens]
        union = set.intersection(*indexes)
        return len(union)

