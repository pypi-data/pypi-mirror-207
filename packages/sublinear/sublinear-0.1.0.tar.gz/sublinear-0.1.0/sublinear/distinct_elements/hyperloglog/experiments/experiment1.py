from ..hyper_log_log import HyperLogLog
import sys

def test_hll():
    hll = HyperLogLog(16) # Initialize HyperLogLog with 16-bit bucket address

    num_elements = 100000

    test2 = []
    for i in range(num_elements):
        test2 += [f"word{i}"]

    for item in test2:
        hll.add(item)

    cardinality = hll.estimate_cardinality()

    print(f"Estimated number of distinct elements: {cardinality}")

    print(f"Actual number of distinct elements: {num_elements}")