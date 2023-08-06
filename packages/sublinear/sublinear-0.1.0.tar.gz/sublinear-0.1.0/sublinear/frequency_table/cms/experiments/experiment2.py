# Experiment 2 (Romeo and Juliet)

from .cms_text import CMS_Text
import os

def test_cms_2():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_path = "../data/romeo-and-juliet.txt"
    file_path = os.path.join(current_dir, relative_path)

    def test_1():
        print("Test 1")
        print("epsilon = 0.01, delta = 0.05")
        print(100 * "-")
        test = CMS_Text(0.01, 0.05, file_path)
        test.run()
        test.plot_error()
        print()

    def test_2():
        print("Test 2")
        print("epsilon = 0.005, delta = 0.05")
        print(100 * "-")
        test = CMS_Text(0.005, 0.05, file_path)
        test.run()
        test.plot_error()
        print()

    def test_3():
        print("Test 3")
        print("epsilon = 0.005, delta = 0.001")
        print(100 * "-")
        test = CMS_Text(0.005, 0.01, file_path)
        test.run()
        test.plot_error()
        print()

    def test_4():
        print("Test 4")
        print("epsilon = 0.1, delta = 0.01")
        print(100 * "-")
        test = CMS_Text(0.1, 0.01, file_path)
        test.run()
        test.plot_error()
        print()

    test_1()
    test_2()
    test_3()
    test_4()