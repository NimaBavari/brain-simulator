import random


def freq_feeder():
    # Can be replaced by a custom generator
    while True:
        yield random.uniform(0, 1000)


def event_feeder():
    # Can be replaced by a custom generator
    while True:
        yield random.randint(0, 2**64 - 1)
