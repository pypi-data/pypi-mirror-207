from ..morris_plus_plus import MorrisPlusPlusCounter
from ..morris_plus import MorrisPlusCounter
from ..morris_basic import MorrisCounter

def test_morris():
    morris = MorrisCounter()
    test_stream = [i for i in range(100)]

    morris.process_stream(test_stream)
    estimate = morris.estimate_count()

    print(f"Morris:   Estimated count of elements: {estimate}")

    s = 10
    morris_plus = MorrisPlusCounter(s)

    morris_plus.process_stream(test_stream)
    estimate = morris_plus.estimate_count()

    print(f"Morris+:  Estimated count of elements: {estimate}")

    epsilon = 0.1
    delta = 0.1
    morris_plus_plus = MorrisPlusPlusCounter(epsilon, delta)

    morris_plus_plus.process_stream(test_stream)
    estimate = morris_plus_plus.estimate_count()

    print(f"Morris++: Estimated count of elements: {estimate}")

    print(f"Actual count of elements: {len(test_stream)}")

