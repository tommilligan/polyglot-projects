from math import floor
import random

from faker import Faker

LINE_LENGTH_MU = 20
LINE_LENGTH_SIGMA = 5
LINES = 10000
SEED = 'cooccurrence'

# Seed
fake = Faker()
fake.seed(SEED)
random.seed(SEED)

for i in range(LINES):
    line_length = max(0, floor(random.gauss(LINE_LENGTH_MU, LINE_LENGTH_SIGMA)))
    line = " ".join([fake.first_name() for j in range(line_length)])
    print(line)

