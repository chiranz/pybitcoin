import unittest
from unittest import TestSuite, TextTestRunner, makeSuite
from Tests.ecc_test import ECCTest
from Tests.field_element_test import FieldElementTest
from Tests.point_test import PointTest


tests = [ECCTest, FieldElementTest, PointTest]


def suite(tests):

    test_suite = TestSuite()
    for test in tests:
        test_suite.addTest(makeSuite(test))
    return test_suite


mySuit = suite(tests)
runner = TextTestRunner()
runner.run(mySuit)
