import unittest
from unittest import TestSuite, TextTestRunner, makeSuite
from Tests.ecc_test import ECCTest
from Tests.field_element_test import FieldElementTest
from Tests.point_test import PointTest
from Tests.s256_test import S256Test, PrivateKeyTest


tests = [ECCTest, FieldElementTest, PointTest, S256Test, PrivateKeyTest]


def suite(tests):

    test_suite = TestSuite()
    for test in tests:
        test_suite.addTest(makeSuite(test))
    return test_suite


mySuit = suite(tests)
runner = TextTestRunner()
runner.run(mySuit)
