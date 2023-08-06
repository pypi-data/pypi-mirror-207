from collections import Counter
from ..ams_sketch_plus import AMSSketchPlus

def test_ams_2():
    # Create a test stream
    test_stream = [i % 10 for i in range(10000)]

    # Initialize AMS Sketch 2
    epsilon = 0.1
    ams2 = AMSSketchPlus(10, epsilon)

    # Process the stream
    ams2.process_stream(test_stream)

    # Estimate the second moment
    estimated_second_moment_2 = ams2.get_estimate()

    print("Estimated second moment:", estimated_second_moment_2)

    # Compute the frequencies of unique elements in the stream
    element_frequencies = Counter(test_stream)

    # Calculate the actual second moment
    actual_second_moment = sum(freq ** 2 for freq in element_frequencies.values())

    print("Actual second moment:", actual_second_moment)
